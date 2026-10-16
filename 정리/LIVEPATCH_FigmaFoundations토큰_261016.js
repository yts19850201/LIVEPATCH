/**
 * createVariableCollection
 *
 * Creates a new Figma variable collection with the specified name and modes.
 * If `modeNames` has more than one entry, the first mode is renamed from
 * Figma's default "Mode 1" to the first name, and additional modes are added.
 *
 * @param {string} name - The display name of the collection (e.g. "Color", "Spacing").
 * @param {string[]} modeNames - Ordered list of mode names (e.g. ["Light", "Dark"] or ["Value"]).
 * @returns {Promise<{
 *   collection: VariableCollection,
 *   modeIds: Record<string, string>
 * }>}
 *   `modeIds` maps each mode name to its modeId string.
 */
async function createVariableCollection(name, modeNames) {
  if (!modeNames || modeNames.length === 0) {
    throw new Error('createVariableCollection: modeNames must have at least one entry.')
  }

  // Create the collection — Figma always creates it with one mode named "Mode 1".
  const collection = figma.variables.createVariableCollection(name)

  // modeIds accumulator
  const modeIds = {}

  // Rename the default first mode
  const defaultMode = collection.modes[0]
  collection.renameMode(defaultMode.modeId, modeNames[0])
  modeIds[modeNames[0]] = defaultMode.modeId

  // Add additional modes
  for (let i = 1; i < modeNames.length; i++) {
    const newModeId = collection.addMode(modeNames[i])
    modeIds[modeNames[i]] = newModeId
  }

  return { collection, modeIds }
}

/**
 * createSemanticTokens
 *
 * Creates a batch of Figma variables in the given collection, one per entry in
 * `tokenMap`. Supports raw values, variable alias references, code syntax, and
 * scopes. Returns a map of token name → Variable for use in subsequent steps.
 *
 * @param {VariableCollection} collection - The target variable collection.
 * @param {Record<string, string>} modeIds - Map of {modeName: modeId} from createVariableCollection.
 * @param {Array<{
 *   name: string,
 *   type: 'COLOR' | 'FLOAT' | 'STRING' | 'BOOLEAN' | 'TIMING' | 'EASING',
 *   values: Record<string, string | number | boolean | MotionEasing | {type: 'VARIABLE_ALIAS', id: string}>,
 *   scopes?: VariableScope[],
 *   codeSyntax?: {WEB?: string, ANDROID?: string, iOS?: string}
 * }>} tokenMap - Ordered list of token definitions.
 *   - `name`: Variable name using slash hierarchy (e.g. "color/bg/primary").
 *   - `type`: Figma variable type.
 *   - `values`: Map of {modeName: value}. Values can be raw (hex string for COLOR,
 *     number for FLOAT) or alias objects {type: 'VARIABLE_ALIAS', id: variableId}.
 *     For COLOR, raw values are accepted as hex strings ("#rrggbb" or "#rrggbbaa")
 *     and converted to {r, g, b, a} automatically.
 *   - `scopes`: Array of VariableScope strings. Omit to use [] (hidden/primitive).
 *   - `codeSyntax`: Platform code syntax strings. Omit to skip.
 * @returns {Promise<{variables: Record<string, Variable>}>}
 *   `variables` maps each token name to its created Variable object.
 */
async function createSemanticTokens(collection, modeIds, tokenMap) {
  const variables = {}

  for (const token of tokenMap) {
    // Create the variable
    const variable = figma.variables.createVariable(token.name, collection, token.type)

    // Set values for each mode
    for (const [modeName, rawValue] of Object.entries(token.values)) {
      const modeId = modeIds[modeName]
      if (!modeId) {
        throw new Error(
          `createSemanticTokens: mode "${modeName}" not found in modeIds for token "${token.name}". ` +
            `Available modes: ${Object.keys(modeIds).join(', ')}`,
        )
      }

      let value = rawValue

      // Convert hex strings to Figma RGBA for COLOR type
      if (token.type === 'COLOR' && typeof rawValue === 'string' && rawValue.startsWith('#')) {
        value = hexToFigmaColor(rawValue)
      }

      variable.setValueForMode(modeId, value)
    }

    // Set scopes (default: empty array = hidden from property pickers / primitives)
    variable.scopes = token.scopes || []

    // Set code syntax per platform
    if (token.codeSyntax) {
      if (token.codeSyntax.WEB) {
        variable.setVariableCodeSyntax('WEB', token.codeSyntax.WEB)
      }
      if (token.codeSyntax.ANDROID) {
        variable.setVariableCodeSyntax('ANDROID', token.codeSyntax.ANDROID)
      }
      if (token.codeSyntax.iOS) {
        variable.setVariableCodeSyntax('iOS', token.codeSyntax.iOS)
      }
    }

    variables[token.name] = variable
  }

  return { variables }
}

/**
 * Converts a hex color string to a Figma RGBA object.
 * Supports "#rgb", "#rrggbb", and "#rrggbbaa".
 *
 * @param {string} hex
 * @returns {{ r: number, g: number, b: number, a: number }}
 */
function hexToFigmaColor(hex) {
  let h = hex.replace('#', '')

  // Expand shorthand #rgb → #rrggbb
  if (h.length === 3) {
    h = h
      .split('')
      .map((c) => c + c)
      .join('')
  }

  const r = parseInt(h.substring(0, 2), 16) / 255
  const g = parseInt(h.substring(2, 4), 16) / 255
  const b = parseInt(h.substring(4, 6), 16) / 255
  const a = h.length === 8 ? parseInt(h.substring(6, 8), 16) / 255 : 1

  return { r, g, b, a }
}

const SOURCE={"version": "1.0", "date": "2026-10-16", "scope": "Foundations only", "frame": 1920, "content": 1440, "font": "Pretendard", "tokens": [{"css": "--font-weight-regular", "name": "font-weight-regular", "type": "FLOAT", "group": "Typography", "value": 400.0, "alias_css": null, "scopes": ["FONT_WEIGHT"]}, {"css": "--font-weight-medium", "name": "font-weight-medium", "type": "FLOAT", "group": "Typography", "value": 500.0, "alias_css": null, "scopes": ["FONT_WEIGHT"]}, {"css": "--font-weight-semibold", "name": "font-weight-semibold", "type": "FLOAT", "group": "Typography", "value": 600.0, "alias_css": null, "scopes": ["FONT_WEIGHT"]}, {"css": "--font-weight-bold", "name": "font-weight-bold", "type": "FLOAT", "group": "Typography", "value": 700.0, "alias_css": null, "scopes": ["FONT_WEIGHT"]}, {"css": "--text-display", "name": "text-display", "type": "FLOAT", "group": "Typography", "value": 48.0, "alias_css": null, "scopes": ["FONT_SIZE"]}, {"css": "--text-h1", "name": "text-h1", "type": "FLOAT", "group": "Typography", "value": 32.0, "alias_css": null, "scopes": ["FONT_SIZE"]}, {"css": "--text-h2", "name": "text-h2", "type": "FLOAT", "group": "Typography", "value": 24.0, "alias_css": null, "scopes": ["FONT_SIZE"]}, {"css": "--text-h3", "name": "text-h3", "type": "FLOAT", "group": "Typography", "value": 20.0, "alias_css": null, "scopes": ["FONT_SIZE"]}, {"css": "--text-h4", "name": "text-h4", "type": "FLOAT", "group": "Typography", "value": 18.0, "alias_css": null, "scopes": ["FONT_SIZE"]}, {"css": "--text-body-lg", "name": "text-body-lg", "type": "FLOAT", "group": "Typography", "value": 18.0, "alias_css": null, "scopes": ["FONT_SIZE"]}, {"css": "--text-body", "name": "text-body", "type": "FLOAT", "group": "Typography", "value": 16.0, "alias_css": null, "scopes": ["FONT_SIZE"]}, {"css": "--text-body-sm", "name": "text-body-sm", "type": "FLOAT", "group": "Typography", "value": 14.0, "alias_css": null, "scopes": ["FONT_SIZE"]}, {"css": "--text-caption", "name": "text-caption", "type": "FLOAT", "group": "Typography", "value": 13.0, "alias_css": null, "scopes": ["FONT_SIZE"]}, {"css": "--leading-display", "name": "leading-display", "type": "FLOAT", "group": "Typography", "value": 1.25, "alias_css": null, "scopes": []}, {"css": "--leading-heading", "name": "leading-heading", "type": "FLOAT", "group": "Typography", "value": 1.3125, "alias_css": null, "scopes": []}, {"css": "--leading-body", "name": "leading-body", "type": "FLOAT", "group": "Typography", "value": 1.625, "alias_css": null, "scopes": []}, {"css": "--leading-caption", "name": "leading-caption", "type": "FLOAT", "group": "Typography", "value": 1.538462, "alias_css": null, "scopes": []}, {"css": "--project-primary", "name": "project-primary", "type": "COLOR", "group": "Color", "value": "#2563eb", "alias_css": null, "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--project-primary-hover", "name": "project-primary-hover", "type": "COLOR", "group": "Color", "value": "#1d4ed8", "alias_css": null, "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--project-primary-active", "name": "project-primary-active", "type": "COLOR", "group": "Color", "value": "#1e40af", "alias_css": null, "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--project-primary-soft", "name": "project-primary-soft", "type": "COLOR", "group": "Color", "value": "#eff6ff", "alias_css": null, "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--project-accent", "name": "project-accent", "type": "COLOR", "group": "Color", "value": "#2563eb", "alias_css": "--project-primary", "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--project-accent-soft", "name": "project-accent-soft", "type": "COLOR", "group": "Color", "value": "#eff6ff", "alias_css": "--project-primary-soft", "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-ink-950", "name": "color-ink-950", "type": "COLOR", "group": "Color", "value": "#111317", "alias_css": null, "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-ink-900", "name": "color-ink-900", "type": "COLOR", "group": "Color", "value": "#191c21", "alias_css": null, "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-ink-800", "name": "color-ink-800", "type": "COLOR", "group": "Color", "value": "#272b31", "alias_css": null, "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-ink-700", "name": "color-ink-700", "type": "COLOR", "group": "Color", "value": "#3b4048", "alias_css": null, "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-ink-600", "name": "color-ink-600", "type": "COLOR", "group": "Color", "value": "#555c66", "alias_css": null, "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-ink-500", "name": "color-ink-500", "type": "COLOR", "group": "Color", "value": "#747c88", "alias_css": null, "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-ink-400", "name": "color-ink-400", "type": "COLOR", "group": "Color", "value": "#9aa1ab", "alias_css": null, "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-white", "name": "color-white", "type": "COLOR", "group": "Color", "value": "#ffffff", "alias_css": null, "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-bg", "name": "color-bg", "type": "COLOR", "group": "Color", "value": "#ffffff", "alias_css": null, "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-bg-warm", "name": "color-bg-warm", "type": "COLOR", "group": "Color", "value": "#fbfaf8", "alias_css": null, "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-bg-subtle", "name": "color-bg-subtle", "type": "COLOR", "group": "Color", "value": "#f7f8fa", "alias_css": null, "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-bg-muted", "name": "color-bg-muted", "type": "COLOR", "group": "Color", "value": "#f0f2f5", "alias_css": null, "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-bg-inverse", "name": "color-bg-inverse", "type": "COLOR", "group": "Color", "value": "#17191d", "alias_css": null, "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-text-strong", "name": "color-text-strong", "type": "COLOR", "group": "Color", "value": "#111317", "alias_css": "--color-ink-950", "scopes": ["TEXT_FILL"]}, {"css": "--color-text", "name": "color-text", "type": "COLOR", "group": "Color", "value": "#3b4048", "alias_css": "--color-ink-700", "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-text-muted", "name": "color-text-muted", "type": "COLOR", "group": "Color", "value": "#555c66", "alias_css": "--color-ink-600", "scopes": ["TEXT_FILL"]}, {"css": "--color-text-disabled", "name": "color-text-disabled", "type": "COLOR", "group": "Color", "value": "#9aa1ab", "alias_css": "--color-ink-400", "scopes": ["TEXT_FILL"]}, {"css": "--color-text-inverse", "name": "color-text-inverse", "type": "COLOR", "group": "Color", "value": "#ffffff", "alias_css": null, "scopes": ["TEXT_FILL"]}, {"css": "--color-line-light", "name": "color-line-light", "type": "COLOR", "group": "Color", "value": "#eceef1", "alias_css": null, "scopes": ["STROKE_COLOR"]}, {"css": "--color-line", "name": "color-line", "type": "COLOR", "group": "Color", "value": "#dde1e6", "alias_css": null, "scopes": ["STROKE_COLOR"]}, {"css": "--color-line-strong", "name": "color-line-strong", "type": "COLOR", "group": "Color", "value": "#c9cfd7", "alias_css": null, "scopes": ["STROKE_COLOR"]}, {"css": "--color-success", "name": "color-success", "type": "COLOR", "group": "Color", "value": "#3b4048", "alias_css": "--color-ink-700", "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-success-soft", "name": "color-success-soft", "type": "COLOR", "group": "Color", "value": "#f7f8fa", "alias_css": "--color-bg-subtle", "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-warning", "name": "color-warning", "type": "COLOR", "group": "Color", "value": "#555c66", "alias_css": "--color-ink-600", "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-warning-soft", "name": "color-warning-soft", "type": "COLOR", "group": "Color", "value": "#f7f8fa", "alias_css": "--color-bg-subtle", "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-error", "name": "color-error", "type": "COLOR", "group": "Color", "value": "#c93636", "alias_css": null, "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-error-soft", "name": "color-error-soft", "type": "COLOR", "group": "Color", "value": "#fff0f0", "alias_css": null, "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-info", "name": "color-info", "type": "COLOR", "group": "Color", "value": "#3b4048", "alias_css": "--color-ink-700", "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--color-info-soft", "name": "color-info-soft", "type": "COLOR", "group": "Color", "value": "#f7f8fa", "alias_css": "--color-bg-subtle", "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--space-1", "name": "space-1", "type": "FLOAT", "group": "Metrics", "value": 4.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--space-2", "name": "space-2", "type": "FLOAT", "group": "Metrics", "value": 8.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--space-3", "name": "space-3", "type": "FLOAT", "group": "Metrics", "value": 12.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--space-4", "name": "space-4", "type": "FLOAT", "group": "Metrics", "value": 16.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--space-5", "name": "space-5", "type": "FLOAT", "group": "Metrics", "value": 20.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--space-6", "name": "space-6", "type": "FLOAT", "group": "Metrics", "value": 24.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--space-7", "name": "space-7", "type": "FLOAT", "group": "Metrics", "value": 28.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--space-8", "name": "space-8", "type": "FLOAT", "group": "Metrics", "value": 32.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--space-10", "name": "space-10", "type": "FLOAT", "group": "Metrics", "value": 40.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--space-12", "name": "space-12", "type": "FLOAT", "group": "Metrics", "value": 48.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--space-14", "name": "space-14", "type": "FLOAT", "group": "Metrics", "value": 56.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--space-16", "name": "space-16", "type": "FLOAT", "group": "Metrics", "value": 64.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--space-18", "name": "space-18", "type": "FLOAT", "group": "Metrics", "value": 72.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--space-20", "name": "space-20", "type": "FLOAT", "group": "Metrics", "value": 80.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--space-24", "name": "space-24", "type": "FLOAT", "group": "Metrics", "value": 96.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--space-28", "name": "space-28", "type": "FLOAT", "group": "Metrics", "value": 112.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--container-main", "name": "container-main", "type": "FLOAT", "group": "Metrics", "value": 1440.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--container-content", "name": "container-content", "type": "FLOAT", "group": "Metrics", "value": 1200.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--container-wide", "name": "container-wide", "type": "FLOAT", "group": "Metrics", "value": 1440.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--content-reading", "name": "content-reading", "type": "FLOAT", "group": "Metrics", "value": 736.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--content-reading-wide", "name": "content-reading-wide", "type": "FLOAT", "group": "Metrics", "value": 880.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--page-gutter", "name": "page-gutter", "type": "FLOAT", "group": "Metrics", "value": 40.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--section-space-xl", "name": "section-space-xl", "type": "FLOAT", "group": "Metrics", "value": 104.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--section-space-lg", "name": "section-space-lg", "type": "FLOAT", "group": "Metrics", "value": 88.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--section-space-md", "name": "section-space-md", "type": "FLOAT", "group": "Metrics", "value": 72.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--section-space-sm", "name": "section-space-sm", "type": "FLOAT", "group": "Metrics", "value": 56.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--grid-gap", "name": "grid-gap", "type": "FLOAT", "group": "Metrics", "value": 24.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--grid-gap-lg", "name": "grid-gap-lg", "type": "FLOAT", "group": "Metrics", "value": 32.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--radius-control", "name": "radius-control", "type": "FLOAT", "group": "Metrics", "value": 10.0, "alias_css": null, "scopes": ["CORNER_RADIUS"]}, {"css": "--radius-card", "name": "radius-card", "type": "FLOAT", "group": "Metrics", "value": 12.0, "alias_css": null, "scopes": ["CORNER_RADIUS"]}, {"css": "--radius-media", "name": "radius-media", "type": "FLOAT", "group": "Metrics", "value": 16.0, "alias_css": null, "scopes": ["CORNER_RADIUS"]}, {"css": "--radius-feature", "name": "radius-feature", "type": "FLOAT", "group": "Metrics", "value": 20.0, "alias_css": null, "scopes": ["CORNER_RADIUS"]}, {"css": "--radius-pill", "name": "radius-pill", "type": "FLOAT", "group": "Metrics", "value": 999.0, "alias_css": null, "scopes": ["CORNER_RADIUS"]}, {"css": "--control-height-sm", "name": "control-height-sm", "type": "FLOAT", "group": "Metrics", "value": 40.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--control-height-md", "name": "control-height-md", "type": "FLOAT", "group": "Metrics", "value": 46.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--control-height-lg", "name": "control-height-lg", "type": "FLOAT", "group": "Metrics", "value": 52.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--header-height-desktop", "name": "header-height-desktop", "type": "FLOAT", "group": "Metrics", "value": 80.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--header-height-mobile", "name": "header-height-mobile", "type": "FLOAT", "group": "Metrics", "value": 60.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--focus-ring-color", "name": "focus-ring-color", "type": "COLOR", "group": "Color", "value": "#2563eb", "alias_css": "--project-primary", "scopes": ["STROKE_COLOR"]}, {"css": "--focus-ring-width", "name": "focus-ring-width", "type": "FLOAT", "group": "Metrics", "value": 3.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--focus-ring-offset", "name": "focus-ring-offset", "type": "FLOAT", "group": "Metrics", "value": 2.0, "alias_css": null, "scopes": []}, {"css": "--duration-fast", "name": "duration-fast", "type": "FLOAT", "group": "Metrics", "value": 160.0, "alias_css": null, "scopes": []}, {"css": "--duration-normal", "name": "duration-normal", "type": "FLOAT", "group": "Metrics", "value": 240.0, "alias_css": null, "scopes": []}, {"css": "--duration-slow", "name": "duration-slow", "type": "FLOAT", "group": "Metrics", "value": 360.0, "alias_css": null, "scopes": []}, {"css": "--z-base", "name": "z-base", "type": "FLOAT", "group": "Metrics", "value": 0.0, "alias_css": null, "scopes": []}, {"css": "--z-sticky", "name": "z-sticky", "type": "FLOAT", "group": "Metrics", "value": 50.0, "alias_css": null, "scopes": []}, {"css": "--z-header", "name": "z-header", "type": "FLOAT", "group": "Metrics", "value": 100.0, "alias_css": null, "scopes": []}, {"css": "--z-dropdown", "name": "z-dropdown", "type": "FLOAT", "group": "Metrics", "value": 200.0, "alias_css": null, "scopes": []}, {"css": "--z-modal", "name": "z-modal", "type": "FLOAT", "group": "Metrics", "value": 300.0, "alias_css": null, "scopes": []}, {"css": "--z-toast", "name": "z-toast", "type": "FLOAT", "group": "Metrics", "value": 400.0, "alias_css": null, "scopes": []}, {"css": "--ratio-avatar", "name": "ratio-avatar", "type": "FLOAT", "group": "Metrics", "value": 1.0, "alias_css": null, "scopes": []}, {"css": "--color-text-action", "name": "color-text-action", "type": "COLOR", "group": "Color", "value": "#2563eb", "alias_css": "--project-primary", "scopes": ["TEXT_FILL"]}, {"css": "--color-text-on-primary", "name": "color-text-on-primary", "type": "COLOR", "group": "Color", "value": "#ffffff", "alias_css": "--color-white", "scopes": ["TEXT_FILL"]}, {"css": "--color-line-control", "name": "color-line-control", "type": "COLOR", "group": "Color", "value": "#747c88", "alias_css": "--color-ink-500", "scopes": ["STROKE_COLOR"]}, {"css": "--frame-desktop", "name": "frame-desktop", "type": "FLOAT", "group": "Metrics", "value": 1920.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--frame-content-margin", "name": "frame-content-margin", "type": "FLOAT", "group": "Metrics", "value": 240.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--layout-columns", "name": "layout-columns", "type": "FLOAT", "group": "Metrics", "value": 12.0, "alias_css": null, "scopes": []}, {"css": "--control-hit-min", "name": "control-hit-min", "type": "FLOAT", "group": "Metrics", "value": 44.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--studio-topbar-height", "name": "studio-topbar-height", "type": "FLOAT", "group": "Metrics", "value": 56.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--studio-dock-width-collapsed", "name": "studio-dock-width-collapsed", "type": "FLOAT", "group": "Metrics", "value": 320.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--studio-dock-width-expanded", "name": "studio-dock-width-expanded", "type": "FLOAT", "group": "Metrics", "value": 380.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--studio-dock-height-collapsed", "name": "studio-dock-height-collapsed", "type": "FLOAT", "group": "Metrics", "value": 56.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--studio-inspector-width", "name": "studio-inspector-width", "type": "FLOAT", "group": "Metrics", "value": 380.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--studio-inspector-min", "name": "studio-inspector-min", "type": "FLOAT", "group": "Metrics", "value": 360.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--studio-inspector-max", "name": "studio-inspector-max", "type": "FLOAT", "group": "Metrics", "value": 420.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--studio-safe-area", "name": "studio-safe-area", "type": "FLOAT", "group": "Metrics", "value": 16.0, "alias_css": null, "scopes": ["GAP"]}, {"css": "--studio-chrome-bg", "name": "studio-chrome-bg", "type": "COLOR", "group": "Color", "value": "#ffffff", "alias_css": "--color-bg", "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--studio-canvas-bg", "name": "studio-canvas-bg", "type": "COLOR", "group": "Color", "value": "#f0f2f5", "alias_css": "--color-bg-muted", "scopes": ["FRAME_FILL", "SHAPE_FILL"]}, {"css": "--studio-selection", "name": "studio-selection", "type": "COLOR", "group": "Color", "value": "#2563eb", "alias_css": "--project-primary", "scopes": ["STROKE_COLOR"]}, {"css": "--studio-patched", "name": "studio-patched", "type": "COLOR", "group": "Color", "value": "#3b4048", "alias_css": "--color-text", "scopes": ["STROKE_COLOR"]}, {"css": "--studio-ambiguous", "name": "studio-ambiguous", "type": "COLOR", "group": "Color", "value": "#555c66", "alias_css": "--color-text-muted", "scopes": ["STROKE_COLOR"]}, {"css": "--studio-blocked", "name": "studio-blocked", "type": "COLOR", "group": "Color", "value": "#c93636", "alias_css": "--color-error", "scopes": ["STROKE_COLOR"]}, {"css": "--studio-ring-width", "name": "studio-ring-width", "type": "FLOAT", "group": "Metrics", "value": 2.0, "alias_css": null, "scopes": ["WIDTH_HEIGHT"]}, {"css": "--studio-ring-outer", "name": "studio-ring-outer", "type": "FLOAT", "group": "Metrics", "value": 1.0, "alias_css": null, "scopes": []}, {"css": "--line-display", "name": "line-display", "type": "FLOAT", "group": "Typography", "value": 60.0, "alias_css": null, "scopes": ["LINE_HEIGHT"]}, {"css": "--line-h1", "name": "line-h1", "type": "FLOAT", "group": "Typography", "value": 42.0, "alias_css": null, "scopes": ["LINE_HEIGHT"]}, {"css": "--line-h2", "name": "line-h2", "type": "FLOAT", "group": "Typography", "value": 34.0, "alias_css": null, "scopes": ["LINE_HEIGHT"]}, {"css": "--line-h3", "name": "line-h3", "type": "FLOAT", "group": "Typography", "value": 28.0, "alias_css": null, "scopes": ["LINE_HEIGHT"]}, {"css": "--line-h4", "name": "line-h4", "type": "FLOAT", "group": "Typography", "value": 26.0, "alias_css": null, "scopes": ["LINE_HEIGHT"]}, {"css": "--line-body-lg", "name": "line-body-lg", "type": "FLOAT", "group": "Typography", "value": 28.0, "alias_css": null, "scopes": ["LINE_HEIGHT"]}, {"css": "--line-body", "name": "line-body", "type": "FLOAT", "group": "Typography", "value": 26.0, "alias_css": null, "scopes": ["LINE_HEIGHT"]}, {"css": "--line-body-sm", "name": "line-body-sm", "type": "FLOAT", "group": "Typography", "value": 22.0, "alias_css": null, "scopes": ["LINE_HEIGHT"]}, {"css": "--line-caption", "name": "line-caption", "type": "FLOAT", "group": "Typography", "value": 20.0, "alias_css": null, "scopes": ["LINE_HEIGHT"]}, {"css": "--text-label", "name": "text-label", "type": "FLOAT", "group": "Typography", "value": 14.0, "alias_css": null, "scopes": ["FONT_SIZE"]}, {"css": "--line-label", "name": "line-label", "type": "FLOAT", "group": "Typography", "value": 20.0, "alias_css": null, "scopes": ["LINE_HEIGHT"]}, {"css": "--font-sans", "name": "font-sans", "type": "STRING", "group": "Typography", "value": "Pretendard", "alias_css": null, "scopes": ["FONT_FAMILY"]}, {"css": "--font-display", "name": "font-display", "type": "STRING", "group": "Typography", "value": "Pretendard", "alias_css": "--font-sans", "scopes": ["FONT_FAMILY"]}], "text_styles": [{"name": "LP Display", "size": 48, "line": 60, "weight": "Bold", "size_css": "--text-display", "line_css": "--line-display"}, {"name": "LP H1", "size": 32, "line": 42, "weight": "Bold", "size_css": "--text-h1", "line_css": "--line-h1"}, {"name": "LP H2", "size": 24, "line": 34, "weight": "SemiBold", "size_css": "--text-h2", "line_css": "--line-h2"}, {"name": "LP H3", "size": 20, "line": 28, "weight": "SemiBold", "size_css": "--text-h3", "line_css": "--line-h3"}, {"name": "LP H4", "size": 18, "line": 26, "weight": "SemiBold", "size_css": "--text-h4", "line_css": "--line-h4"}, {"name": "LP Body Large", "size": 18, "line": 28, "weight": "Regular", "size_css": "--text-body-lg", "line_css": "--line-body-lg"}, {"name": "LP Body", "size": 16, "line": 26, "weight": "Regular", "size_css": "--text-body", "line_css": "--line-body"}, {"name": "LP Body Small", "size": 14, "line": 22, "weight": "Regular", "size_css": "--text-body-sm", "line_css": "--line-body-sm"}, {"name": "LP Caption", "size": 13, "line": 20, "weight": "Regular", "size_css": "--text-caption", "line_css": "--line-caption"}, {"name": "LP Label", "size": 14, "line": 20, "weight": "SemiBold", "size_css": "--text-label", "line_css": "--line-label"}]};

const existing = await figma.variables.getLocalVariableCollectionsAsync();
if(existing.some(c=>c.name.startsWith('LP '))) throw new Error('LP collections already exist. Read state and reconcile before creation.');
await Promise.all(['Regular','Medium','SemiBold','Bold'].map(style=>figma.loadFontAsync({family:'Pretendard',style})));
const ledger={runId:'livepatch-foundations-261016',scope:'Foundations only',fileKey:'VwuyN75CQK9Kn0ZyIVmF4S',step:'tokens-created',entities:{collections:{},variables:{},primitives:{},textStyles:{},effectStyles:{}},completedSteps:['discovery'],pendingValidations:['foundations-canvas']};
const cols={};
for(const name of ['Primitives','Color','Metrics','Typography']){
 const {collection,modeIds}=await createVariableCollection('LP '+name,[name==='Color'?'Light':'Value']);cols[name]={collection,modeIds};ledger.entities.collections[name]={id:collection.id,modes:modeIds};
}
const dedup=new Map();const primTokens=[];
for(const token of SOURCE.tokens){const key=token.type+':'+JSON.stringify(token.value);if(dedup.has(key))continue;
 const name=token.type==='COLOR'?'Color '+token.value.replace('#','').toUpperCase():token.type==='STRING'?'Font '+token.value:'Number '+String(token.value).replaceAll('.','p');
 dedup.set(key,name);primTokens.push({name,type:token.type,values:{Value:token.value},scopes:[],codeSyntax:{WEB:'var('+token.css+')'}});
}
const {variables:prims}=await createSemanticTokens(cols.Primitives.collection,cols.Primitives.modeIds,primTokens);
for(const [name,v] of Object.entries(prims))ledger.entities.primitives[name]=v.id;
const vars={};
for(const group of ['Color','Metrics','Typography']){
 const tokens=SOURCE.tokens.filter(t=>t.group===group).map(t=>({name:t.name,type:t.type,values:{[group==='Color'?'Light':'Value']:{type:'VARIABLE_ALIAS',id:prims[dedup.get(t.type+':'+JSON.stringify(t.value))].id}},scopes:t.scopes,codeSyntax:{WEB:'var('+t.css+')'}}));
 const {variables}=await createSemanticTokens(cols[group].collection,cols[group].modeIds,tokens);
 for(const t of SOURCE.tokens.filter(t=>t.group===group)){vars[t.css]=variables[t.name];ledger.entities.variables[t.css]={id:variables[t.name].id};}
}
// 호환/역할 별칭은 직접 semantic token으로 연결한다.
for(const token of SOURCE.tokens.filter(t=>t.alias_css&&vars[t.alias_css])){
 const mode=cols[token.group].modeIds[token.group==='Color'?'Light':'Value'];vars[token.css].setValueForMode(mode,{type:'VARIABLE_ALIAS',id:vars[token.alias_css].id});
}
for(const spec of SOURCE.text_styles){
 const style=figma.createTextStyle();style.name=spec.name;style.fontName={family:'Pretendard',style:spec.weight};style.fontSize=spec.size;style.lineHeight={unit:'PIXELS',value:spec.line};style.letterSpacing={unit:'PERCENT',value:spec.size>=24?-1:0};
 style.setBoundVariable('fontFamily',vars['--font-sans']);style.setBoundVariable('fontSize',vars[spec.size_css]);style.setBoundVariable('lineHeight',vars[spec.line_css]);
 ledger.entities.textStyles[spec.name]={id:style.id,font:spec.weight,size:spec.size,line:spec.line};
}
for(const [name,y,radius,opacity] of [['LP Floating',8,24,.08],['LP Overlay',20,60,.14]]){
 const style=figma.createEffectStyle();style.name=name;style.effects=[{type:'DROP_SHADOW',color:{r:17/255,g:25/255,b:29/255,a:opacity},offset:{x:0,y},radius,spread:0,visible:true,blendMode:'NORMAL'}];ledger.entities.effectStyles[name]=style.id;
}
const all=await figma.variables.getLocalVariablesAsync();const ids=Object.values(ledger.entities.variables).map(v=>v.id);const bad=all.filter(v=>ids.includes(v.id)&&(!v.codeSyntax.WEB||v.scopes.includes('ALL_SCOPES')||!Object.values(v.valuesByMode).every(x=>x&&x.type==='VARIABLE_ALIAS')));
ledger.validation={semanticCount:SOURCE.tokens.length,primitiveCount:primTokens.length,textStyles:SOURCE.text_styles.length,effectStyles:2,badVariableIds:bad.map(v=>v.id)};
ledger.completedSteps.push('tokens-structural-validation');
return {ledger,summary:ledger.validation};
