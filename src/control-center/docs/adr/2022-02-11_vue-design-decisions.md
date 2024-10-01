# Vue.js Design Decisions

Date: 2022-02-11

## State

Decided

## Context

Vue.js can be used in different ways and provided different APIs that can be used.
It can be used with TypeScript or JavaScript and can be bundled by using [webpack](https://webpack.js.org) or [vite](https://vitejs.dev).
Furthermore the [composition API](https://vuejs.org/guide/typescript/composition-api.html) or [options API](https://vuejs.org/guide/typescript/options-api.html) and be used and unit testing can be performed by using [jest](https://jestjs.io) or [vitest](https://vitest.dev).
Last but not least the decision about using [cypress](https://www.cypress.io) and [pinia](https://pinia.vuejs.org) should be hit.

However, the intention of the RI is to provide a basic commonly use setup thats future-proofed and extensible.

## Decision(s)

All the following decisions are based on a [small developer survey](https://forms.office.com/Pages/DesignPage.aspx?fragment=FormId%3DnC2noeZJbU-a9lqvoRg7_emQWhFvZGhMvvpiBFJqWfJUQ0VRWEZaT1k0RTRPTzBJMExFWk8wODBBSC4u%26Token%3D1e6d352adac9424aa9bf15550e3b3321) within the Web Community at DB Systel.
Furthermore the decisions are following the best practices described on [vuejs.org](https://vuejs.org).

### TypeScript instead of JavaScript

As the community echo was clearly for TypeScript and because TypeScript helps to reduce error at build time, we chose TypeScript as main language.

### vite instead of webpack

Vite is choosen as it is the recommended build tool for Vue.js 3 apps.

**Source:** https://vuejs.org/guide/scaling-up/tooling.html#project-scaffolding

> Vue CLI is the official webpack-based toolchain for Vue. It is now in maintenance mode and we recommend starting new projects with Vite unless you rely on specific webpack-only features. Vite will provide superior developer experience in most cases.

Another good thing is that SCSS Support comes out-of-the-box

**Source:** https://vitejs.dev/guide/features.html#css-pre-processors

> [...] Vite does provide built-in support for .scss, .sass, .less, .styl and .stylus files. There is no need to install Vite-specific plugins for them, but the corresponding pre-processor itself must be installed

### Composition API instead of Options API

The composition API is the recommended API to use.

**Source:** https://vuejs.org/guide/extras/composition-api-faq.html#better-logic-reuse

> Better Logic Reuse [...]
>
> More Flexible Code Organization [...]
>
> Better Type Inference [...]
>
> Smaller Production Bundle and Less Overhead [...]

### State-Management

Often bigger apps needs a central state-management library, that's why we include the default state-management lib pinia.

### vitest instead of jest

Vitest is the recommended unit testing tool when using vite which is fast and offeres a great DevEx

**Source:** https://vuejs.org/guide/scaling-up/tooling.html#testing

> Vitest is a test runner created by Vue / Vite team members that focuses on speed. It is specifically designed for Vite-based applications to provide the same instant feedback loop for unit / component testing.
>
> Jest can be made to work with Vite via vite-jest. However, this is only recommended if you have existing Jest-based test suites that you need to migrate over to a Vite-based setup, as Vitest provides similar functionalities with a much more efficient integration.

### Cypress for e2e testing

Cypress is a very common e2e testing tool which is also independently from Vue.js.
It will be used as it's recommended in the official vuejs docs and because it provides a great DevEx and good debugging capabilities.

**Source:** https://vuejs.org/guide/scaling-up/tooling.html#testing

> Cypress is recommended for E2E tests. It can also be used for component testing for Vue SFCs via the Cypress Component Test Runner.

## Deciders

Danny Koppenhagen / Web Community Echo
