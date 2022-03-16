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
        fontFamily: {
            sans: [
                'Lato',
                'sans serif',
                'system-ui',
                '-apple-system',
                'BlinkMacSystemFont',
                '"Segoe UI"',
                'Roboto',
                '"Helvetica Neue"',
                'Arial',
                '"Noto Sans"',
                'sans-serif',
                '"Apple Color Emoji"',
                '"Segoe UI Emoji"',
                '"Segoe UI Symbol"',
                '"Noto Color Emoji"',
            ]
        },
        colors: {
            transparent: 'transparent',
            current: 'currentColor',
            white: '#FFFFFF',
            black: '#000000',
            gray: {
                0: '#000000',
                5: '#0d0d0d',
                10: '#1a1a1a',
                15: '#262626',
                20: '#333333',
                25: '#404040',
                30: '#4d4d4d',
                35: '#5a5a5a',
                40: '#666666',
                45: '#737373',
                50: '#808080',
                55: '#8d8d8d',
                60: '#999999',
                65: '#a6a6a6',
                70: '#b3b3b3',
                75: '#c0c0c0',
                80: '#cccccc',
                85: '#d9d9d9',
                90: '#e6e6e6',
                95: '#f2f2f2',
                100: '#ffffff',
            },
            amazon: {
                0: '#000000',
                5: '#050b08',
                10: '#0a1710',
                15: '#0e2218',
                20: '#132e20',
                25: '#183a29',
                30: '#1d4531',
                35: '#225139',
                40: '#265c41',
                45: '#2b6849',
                50: '#307351',
                55: '#458162',
                60: '#598f74',
                65: '#6e9d85',
                70: '#83ab97',
                75: '#98b9a8',
                80: '#acc7b9',
                85: '#c1d5cb',
                90: '#d6e3dc',
                95: '#eaf1ee',
                100: '#ffffff',
            },
            eggplant: {
                0: '#000000',
                5: '#0a0709',
                10: '#130f12',
                15: '#1d161b',
                20: '#261d24',
                25: '#30252d',
                30: '#3a2c36',
                35: '#43333f',
                40: '#43333f',
                45: '#4d3a48',
                50: '#564251',
                55: '#60495a',
                60: '#705b6b',
                65: '#806d7b',
                70: '#90808c',
                75: '#a0929c',
                80: '#b0a4ad',
                85: '#bfb6bd',
                90: '#dfdbde',
                95: '#efedef',
                100: '#ffffff',
            },
            red: {
                0: '#000000',
                5: '#170606',
                10: '#2f0c0c',
                15: '#461111',
                20: '#5d1717',
                25: '#751d1d',
                30: '#8c2323',
                35: '#a32929',
                40: '#ba2e2e',
                45: '#d23434',
                50: '#e93a3a',
                55: '#eb4e4e',
                60: '#ed6161',
                65: '#f07575',
                70: '#f28989',
                75: '#f49d9d',
                80: '#f6b0b0',
                85: '#f8c4c4',
                90: '#fbd8d8',
                95: '#fdebeb',
                100: '#FFFFFF',
            }
        }
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
