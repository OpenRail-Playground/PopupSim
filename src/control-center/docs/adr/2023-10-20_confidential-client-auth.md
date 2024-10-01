# Confidential client auth

Date: 2023-10-20

## State

Decided

Extends:

- [./auth-library.md](./2022-02-21_auth-library.md)

## Context

In order to login via [DB WebSSO](https://db-planet.deutschebahn.com/pages/ipas/apps/content/dbwebsso) or probably other OpenID Connect (OIDC) providers using OAuth2, a secure flow must be used.
This ADR evaluates only the most secure OIDC code flow since other flows are not relevant and should not be used at all.
Therefore the two variants public and confidential client are compared.
Fot more background information about the differences betweeen the flows, please refer to the documentation made by the [Thementeam Web](https://db-inner-source.gitpages.tech.rz.db.de/tt-web/dokumentation-web/Infos/security.html).

## Decision

As a confidential client is the most secure way to authenticate, the recommendation of this approach is followed and we are authenticating against a Backend-for-Frontend which holds the secret and doesn't expose it at any time to the Frontend.
The fact, that a confidential requires a Backend service for authentication can be accepted, as most applications we are developing within the DB, invoking a backend anyway.
If you are forking this project and you are only be able to authenticate as a public client, please check out the previous implementation and the [Auth Library](./2022-02-21_auth-library.md) which was superseded by this ADR but gives you a clue about good potential libraries you can use to setup the public client in your application.

## Alternatives

### OIDC Public Client

The client authenticates directly against the OIDC / Identity provider (IdP).
This must be done using the PKCE extension for OAuth2 to be as most secure as possible.
The frequent exchange of keys guarantees a potential attacker can only access data for a very short time.
However, authenticating with a public client always comes with the drawback, that secrets are hold in the client.
The risk of being attacked can be minimized using PKCE and short living keys but not completely eliminated.

### OIDC Confidential Client

The confidential client authorization flow can only be used when a backend (such as a Backend-For-Frontend - BFF) is available.
This backend acts as a confidential client which established the OIDC flow with the OIDC / Identity provider (IdP).
When successfully authenticated, the BFF established a session with the connected Frontend.
The BFF however does not expose any access or refresh key to the Frontend but uses a session cookie to check the authentication state of the Frontend.
A drawback of this approach is, that it can only be used when a Backend is available which can handle the authentication.

## Deciders

Danny Koppenhagen
Jens Krähmer
