const {themes} = require('prism-react-renderer');

module.exports = {
  title: 'DSA Book',
  url: 'https://soubhikemrs.github.io',
  baseUrl: '/DSA/',
  favicon: 'img/favicon.ico',
  trailingSlash: false,
  
  organizationName: 'soubhikemrs',
  projectName: 'DSA',

  onBrokenLinks: 'throw',

  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          path: 'docs',
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],

  // ADDED: Theme configuration for Code Blocks
  themeConfig: {
    navbar: {
      title: 'DSA Book by Soubhik',
      items: [
        {
          href: 'https://github.com/soubhikemrs/DSA',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    prism: {
      theme: themes.github,        // Light mode code blocks
      darkTheme: themes.dracula,   // Dark mode code blocks
    },
  },
};