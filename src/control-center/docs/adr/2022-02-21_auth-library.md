# Authentication Library

Date: 2022-02-21

## State

Decided

## Context

In order to be able to make use of [DB WebSSO](https://db-planet.deutschebahn.com/pages/ipas/apps/content/dbwebsso) or probably other OpenID Connect (OIDC) providers using OAuth2, an established library should be used.
There are severals found during research which were possibly candidates.
The goal is to redirect the user to the DB Web SSO authentication site and redirect back to the app after a successful Login.

## Decision(s)

After reviewing several libraries, we decided to use the [oidc-client-ts](https://www.npmjs.com/package/oidc-client-ts) lib which is a fork of the [oidc-client](https://www.npmjs.com/package/oidc-client) lib but still in active development.
As it uses TypeScript as well, it comes with good type support.
Even if the package is not directly certified, the forked implementation _oidc-client_ is [certified by the OpenID Foundation](https://openid.net/certification/#RPs).
Furthermore, it's release as Open Source with the Apache 2.0 license.

## Alternatives

**[oidc-client](https://www.npmjs.com/package/oidc-client)**

- not maintained anymore ([Source](https://github.com/IdentityModel/oidc-client-js))
- no new releases since 02/2021 ([Source](https://github.com/IdentityModel/oidc-client-js/releases))
- certified

**[vue-oidc-client](https://www.npmjs.com/package/vue-oidc-client)**

- only a wrapper for the outdated [_oidc-client_](https://www.npmjs.com/package/oidc-client) ([Source](https://github.com/soukoku/vue-oidc-client/blob/master/package.json))
- not certified

**[vuex-oidc](https://www.npmjs.com/package/vuex-oidc)**

- only a wrapper for the outdated [_oidc-client_](https://www.npmjs.com/package/oidc-client) ([Source](https://github.com/soukoku/vue-oidc-client/blob/master/package.json))
- not certified

**[openid-client](https://www.npmjs.com/package/openid-client)**

- certified
- only Node.js, no browser support

## Deciders

Danny Koppenhagen
