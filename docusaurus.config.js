// @ts-check

const config = {
  title: "Use custom docker images in Truss",
  url: "https://rachfop.github.io",
  baseUrl: "/",
  organizationName: "rachfop",
  projectName: "custom-docker-image",

  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: "/",
          sidebarPath: require.resolve("./sidebars.js"),
        },
        blog: false,
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      }),
    ],
  ],
};

module.exports = config;
