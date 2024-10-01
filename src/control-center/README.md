# PopUpSim-ControlCenter

3LH Challenge

## ToDos
- [] Sort tracks based on relative location 

## Architecture

![architecture overview](docs/architecture.drawio.svg)

#### DB UI / DB UX

The styling is based on the [DB UI Core](https://github.com/db-ui/core) library, which implements and follows the [DB UX Design System](https://marketingportal.extranet.deutschebahn.com/marketingportal/Design-Anwendungen/db-ux-design-system).

### ADRs

All architectural decisions are documented in the [docs/adr/](./docs/adr) directory of this project.

## Core Principals

### Best Practices

The source code follows the [Vue Styleguide](https://vuejs.org/style-guide/) as well as general best practices.
We aim to have an evergreen environment with up-to-date package versions and a general compliant setup.
Therefore, [Renovate](https://db.de/renovate) is used to automate dependency and compliant pipeline updates.

### Accessibility

This project contains essential tools to keep your app accessible by ensuring the [WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/) are satisfied.
Further documentation related to accessibility and the implementation in web applications can be found in the [buildIT devEx documentation for accessibility](https://build-it.gitpages.tech.rz.db.de/products/devex-barrierefreiheit/docs/04_Testautomation.html).

#### VSCode extension

The recommended extension [axe Accessibility Linter](https://marketplace.visualstudio.com/items?itemName=deque-systems.vscode-axe-linter)
will help you during development to find accessibility violations.

#### ESLint Rules

The provided ESLint rules (`.eslintrc.cjs`) for a11y, will detect essential accessibility violations.

#### Playwright e2e plugin

The extension [@axe-core/playwright](https://www.npmjs.com/package/@axe-core/playwright) lets [axe](https://github.com/dequelabs/axe-core)
check the current displayed site in Playwright for accessibility violations.

#### pa11y-ci configuration

[Pa11y](https://www.npmjs.com/package/pa11y-ci) runs against a list of URLs and checks these sites for accessibility violations.
Sites to be tested should be explicitly added to the configuration file `.pa11yci`.
The tests are executed in the CI/CD pipeline against the AT (automatic test) environment as well.
Pa11y supports also handing over URLs as parameters or by scanning a `sitemap.xml`.
Please refer to the implementation and [documentation from the provided pa11y-ci job](https://git.tech.rz.db.de/testautomation/pipeship/jobs/pa11y)
of the test automation team.

## How to start?

### Local Development

Start the local development server:

```bash
npm run dev
```

### Build for production

Build the application for (production mode):

```bash
npm build
```

Build the docker image and serve the app (using the [Nginx SPA Image](https://git.tech.rz.db.de/db-inner-source/tt-web/webserver/nginx-spa)):

```bash
docker build -t pop-up-sim-cc . && docker run -p 8080:8080 pop-up-sim-cc
```

## Code Analysis & Quality Assurance

### Linting

The project includes configurations for linting to maintain code quality and consistency.

```bash
npm run lint
```

### Lighthouse

While not the sole focus, [Lighthouse](https://developer.chrome.com/docs/lighthouse) also provides accessibility test results for a list of URLs (see [lighthouserc.cjs](lighthouserc.cjs)).

Lighthouse will be run in CI for each commit and results can be viewed via the [Lighthouse CI server](https://lighthouse.dxc-test.comp.db.de/app/projects/168462/dashboard).

During development one can also run Lighthouse locally.
Accessibility and other violations against defined thresholds will be shown in the results.

```bash
npm run lhci
```

If you do not want to use a third party Lighthouse CI server to collect results remotely, remove the `test_lighthouse_ci` include and configuration from [.gitlab-ci.yml](.gitlab-ci.yml).

### Static Code Analysis

This repo uses SonarQube for static code analysis.
A blueprint for the SonarQube-Server setup can be found in the [TT-inner-source space](https://git.tech.rz.db.de/db-inner-source/helm/sonarqube).

* [Generated Reports](https://sonar-db-inner-source.apps.dbcs-riga.comp.db.de/projects?search=pop-up-sim-cc)

## Testing

### Unit Testing

execute unit tests:

```bash
npm run test
```

execute unit tests and generate code coverage report:

```bash
npm run coverage
```

### e2e Testing

The project is prepared for e2e tests using [Playwright](https://playwright.dev).
The decision for using Playwright by default is documented in [ADR: End-to-End Testing](docs/adr/2023-06-15_end-to-end-testing.md).
E2e tests include tests for authentication with DB WebSSO and an example of how to call a REST API from [Playwright](https://playwright.dev).

```sh
# Install browsers for the first run
npx playwright install

# When testing on CI, must build the project first
npm run build

# Runs the end-to-end tests
npm run test:e2e

# Runs the tests in debug mode
npm run test:e2e:debug

# Runs the tests in trace mode (to time-travel between actions)
npm run test:e2e:trace

# Serve test report (and inspect trace when)
npm run test:e2e:report

# Runs the tests only on Chromium
npm run test:e2e -- --project=chromium
# Runs the tests of a specific file
npm run test:e2e -- tests/example.spec.ts
```

### a11y Testing

The contains essential tools to keep your app accessible,
including Playwright e2e plugin for accessibility checks and pa11y-ci configuration for executing accessibility checks and generating reports.
Playwright tests can be executed as described above in the e2e test step.
The pa11y tests can be executed locally as follows:

```bash
npm run test:a11y
```
