# End-to-End Testing

Date: 2023-06-15

## State

Decided

## Context

End-to-end tests simulate a user's interaction with the application in a real-world scenario, testing it from start to finish.
This captures issues that unit tests or integration tests may overlook. For projects it is therefore important to choose a good
end-to-end testing framework. The framework should support a number of features as outlined in the 'decision drivers' section below.

## Considered Options

The following five options were selected because they were either commonly used in DB projects or have perceived relevance in the industry:

* [Cypress](https://www.cypress.io/)
* [Playwright](https://playwright.dev/)
* [Puppeteer](https://pptr.dev/)
* [TestCafe](https://testcafe.io/)
* [Selenium Webdriver](https://www.npmjs.com/package/selenium-webdriver)

For the RI we did only consider open source frameworks that are meant to be used by developers to write TaC (tests as code).
Teams that prefer tests to be performed by dedicated testers might rather want to use the Systel-proprietary `Xenon framework`
that does not require coding skills but instead is configured through Excel sheets.
For more details on `Xenon` contact [Team `Test Automation`](https://build-it.gitpages.tech.rz.db.de/products/devex-xenon/docs/xenon/xenon_startpage.html).

## Decision Drivers

* **Community Support**<br/>
  The framework should have good community support.
* **Use within Systel**<br/>
  Ideally there should already be (good) experience with the framework in the company.
* **Broad Browser Support**<br/>
  The framework should support a wide variety of browsers (Chrome and Edge support are mandatory).
* **Headless Testing**<br/>
  Tests should be executable in a CI/CD pipeline.
* **Mobile Testing**<br/>
  It should be possible to test web apps for mobile devices such as iOS or Android smartphones or tablets.
* **In-Browser Component Testing**<br/>
  The framework should provide the option to test components (such as React components) *within the browser*
  instead of traditionally within a simulated environment such as JSDom.
* **REST-API Testing**<br/>
  The framework should allow developers to write tests against REST-APIs.
* **Clean Test API**<br/>
  The framework should have a clean test API that allows developer to write terse and to-the-point tests
  that are easy to read and understand.
* **Mocking Network Calls**<br/>
  The framework should provide the option to mock and intercept network calls.
* **Documentation Quality**<br/>
  The framework should be well documented.

## Comparison

The following table compares the five frameworks (June 2023).
All considered frameworks are open-source and do support headless-testing and TypeScript.
They all allow record and playback as well as interactively stepping through tests.

| Aspect / Feature                        | Cypress               | Playwright         | Puppeteer          | TestCafe           | Selenium Webdriver                |
|-----------------------------------------|-----------------------|--------------------|--------------------|--------------------|-----------------------------------|
| Created                                 | 2014                  | 2019               | 2017               | 2015               | 2004                              |
| Backing Company                         | Cypress.io            | Microsoft          | Google             | DevExpress Inc.    | -                                 |
| GitHub Stars                            | 43,6K                 | 52,2K              | 83,6k              | 9,6k               | 26,8k                             |
| Weekly NPM Downloads                    | 5000k                 | 1400k              | 44k                | 9,6k               | 2100k                             |
| Use within Systel                       | heavy                 | moderate           | -                  | -                  | heavy (but mostly older projects) |
| Community Support                       | strong                | strong             | good               | moderate           | strong but receding               |
| Documentation Quality                   | excellent             | excellent          | good               | excellent          | excellent                         |
| Supported Browsers                      | Chrome, Firefox, Edge | All major browsers | Chrome, Firefox    | All major browsers | All major browsers                |
| JavaScript Engine                       | Browser               | Node.js            | Node.js            | Browser            | Both (Node.js and Browser)        |
| Async. (Promise-based) API              | no                    | yes                | yes                | yes                | yes                               |
| API Simplicity/Elegance                 | good                  | very good          | good               | good               | medium                            |
| Mobile Testing                          | no                    | yes, via emulation | yes, via emulation | yes                | yes (using Appium)                |
| REST-API Testing                        | yes                   | yes                | no                 | no                 | no                                |
| In-Browser Component testing            | yes                   | experimental       | no                 | with plugin        | no                                |
| Visual Regression Testing               | 3rd-party             | yes (built-in)     | 3rd-party          | 3rd-party          | 3rd-party                         |
| Network Call Mocking                    | yes                   | yes                | yes                | yes                | no                                |
| Cross-domain Testing (e.g. OAuth2 flow) | limited               | yes                | yes                | limited            | yes                               |
| Automatic Waiting                       | yes                   | yes                | no                 | yes                | no                                |
| Watch Mode (in dev)                     | yes                   | yes                | no                 | yes                | no                                |
| iFrame Support                          | limited               | yes                | yes                | yes                | poor                              |
| Multiple Tabs (Pages)                   | no                    | yes                | yes                | no                 | yes                               |

## Decision

We decide to use **Playwright** as the recommended end-to-end testing framework for the TT-Web RIs.

### Rationale

Playwright already has strong community support even though it is the newest framework of the five.
There are a number of Systel projects that are successfully using Playwright and are quite happy with it.
In contrast to Cypress it comes with support for mobile devices, handles multiple tabs and offers a sleeker, Promise-based API.
Also it does support a broader range of browsers and has better iFrame support.

Selenium Webdriver is the oldest framework of the five and used to be quite prevalent with traditional web applications.
However, it doesn't have as good support for SPAs (which dynamically change the browser DOM) as the newer frameworks have.
For example, there is no support for in-browser component testing, network call mocking, automatic waiting, or watch mode.
And there are reports of synchronization issues and race conditions when used with SPAs as tests are driven from the server
in Selenium. For modern SPAs Playwright therefore is the better option.

We did exclude Puppeteer because it is more geared towards automation (e.g. web scraping) and lacks some of the
more test specific features that Playwright has (such as REST-API testing, automatic waiting, watch mode and in-browser
component testing). Also the download numbers are much lower than for Playwright suggesting low prevalence.

TestCafe finally also was excluded - mainly because it can't compare with the other options in terms
of popularity and breath of community. For example, TestCafe is being downloaded from npm more than 100
times less often than Playwright.

## Deciders

Jens Krähmer, Danny Koppenhagen
