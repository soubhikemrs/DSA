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
      },
    ],
  ],
};