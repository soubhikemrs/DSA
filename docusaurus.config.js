module.exports = {
  title: 'DSA Book',
  url: 'https://soubhikemrs.github.io',
  baseUrl: '/DSA/',
  favicon: 'img/favicon.ico',

  organizationName: 'soubhikemrs',
  projectName: 'DSA',

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