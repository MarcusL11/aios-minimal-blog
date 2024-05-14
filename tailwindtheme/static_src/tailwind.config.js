/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
  content: [
    /**
     * HTML. Paths to Django template files that will contain Tailwind CSS classes.
     */

    /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
    '../templates/**/*.html',

    /*
     * Main templates directory of the project (BASE_DIR/templates).
     * Adjust the following line to match your project structure.
     */
    '../../templates/**/*.html',

    /*
     * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
     * Adjust the following line to match your project structure.
     */
    '../../**/templates/**/*.html',

    /**
     * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
     * patterns match your project structure.
     */
    /* JS 1: Ignore any JavaScript in node_modules folder. */
    // '!../../**/node_modules',
    /* JS 2: Process all JavaScript files in the project. */
    // '../../**/*.js',

    /**
     * Python: If you use Tailwind CSS classes in Python, uncomment the following line
     * and make sure the pattern below matches your project structure.
     */
    // '../../**/*.py'
  ],
  theme: {
    extend: {},
    container: {
      center: true,
      padding: {
        DEFAULT: '1rem',
        sm: '2rem',
        md: '3rem',
        lg: '5rem',
        xl: '8rem',
        '2xl': '10rem',
      },
    },

  },
  daisyui: {
    themes: [
      {
        aios: {
          'primary': '#b3e5fc',
          'primary-focus': '#00796b',
          'primary-content': '#212121',

          'secondary': '#b2dfdb',
          'secondary-focus': '#8bc34a',
          'secondary-content': '#212121',

          'accent': '#a1887f',
          'accent-focus': '#a3aea4',
          'accent-content': '#212121',

          'neutral': '#d5d5d5',
          'neutral-focus': '#9fa4a3',
          'neutral-content': '#212121',

          'base-100': '#fffbeb',
          'base-200': '#f5f5f5',
          'base-300': '#ebebeb',
          'base-content': '#212121',

          'info': '#5dc1c8',
          'success': '#a5d6a7',
          'warning': '#fff59d',
          'error': '#ef9a9a',

          '--rounded-box': '1rem',
          '--rounded-btn': '.5rem',
          '--rounded-badge': '1.9rem',

          '--animation-btn': '.25s',
          '--animation-input': '.2s',

          '--btn-text-case': 'uppercase',
          '--navbar-padding': '.5rem',
          '--border-btn': '1px',
        },
      },
    ],
  },
  plugins: [
    /**
     * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
     * for forms. If you don't like it or have own styling for forms,
     * comment the line below to disable '@tailwindcss/forms'.
     */
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),
    require('daisyui'),
  ],
}
