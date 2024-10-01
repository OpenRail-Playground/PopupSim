# Open Source Licenses (Ril-9184)

Date: 2022-03-03

## State

Decided

## Context

In order to fulfill the requirements of the [Ril-0184](https://dbsw.sharepoint.com/sites/DBSystelDokumente/DB%20Systel%20Dokumente/Forms/Dokumente/docsethomepage.aspx?ID=2236&FolderCTID=0x0120D5200030DD51B1FB83ED4C9F756B5CD03F42160055F017ADF660A74587F7A63B0D2E7AD2&List=a52bb1d8-447e-4097-9b8e-755dd9d80988&RootFolder=%2Fsites%2FDBSystelDokumente%2FDB%20Systel%20Dokumente%2FRil%2D0184%20Open%20Source%20Einsatzrichtlinie&RecSrc=%2Fsites%2FDBSystelDokumente%2FDB%20Systel%20Dokumente%2FRil%2D0184%20Open%20Source%20Einsatzrichtlinie) all dependent open source library licenses must be collected and checked for compliance.
Therefor a tool is needed to:

- a) collect and bundle all license information into a single file
- b) check the dependencies for possible license / compliance violations

To have a flexible solution, the tool should allow to explicitely deny- and allowlist specific libraries.

## Decision(s)

**[rollup-plugin-license](https://www.npmjs.com/package/rollup-plugin-license)**

- available as a plugin for [Rollup](https://rollupjs.org) which is used under the hood of [vite.js](https://vitejs.dev) and directly usable
- MIT License
- collects license information for all dependencies concatenated in a textfile by default
- export format for the information is customizable by providing a template
- provides license check mechanism
- allows deny-/allowlist

### Display licenses information in the imprint section

To show how the collected license information can be used as part of the app, the configuration was made to output the information as a file in the root of the app.
The Apps imprint section loads the content of this file.

## Alternatives

**[webpack-license-plugin](https://www.npmjs.com/package/webpack-license-plugin)**

- MIT License
- collects license information for all dependencies concatenated in a textfile by default
- provides license check mechanism
- allows deny-/allowlist
- available as a plugin for [Webpack](https://webpack.js.org) which is not compatible with [vite.js](https://vitejs.dev)

**[Whitesource](https://dbserviceportal.service-now.com/serviceportal?id=sc_cat_item&sys_id=14c386a5dbab149031998384059619ee)**

- Tool to scan licenses inside the CI/CD Pipeline
- Should be used in addition but does not collect and bundle all licenses into a single artifact file

## Deciders

Danny Koppenhagen
