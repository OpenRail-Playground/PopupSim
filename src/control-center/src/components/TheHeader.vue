<script setup lang="ts">
import { useAuthStore } from '../stores/auth'
import { useI18n } from 'vue-i18n'
import { storeToRefs } from 'pinia'

const { locale } = useI18n()
const auth = useAuthStore()
const { isAuthenticated } = storeToRefs(auth)

const { login, logout } = auth
</script>

<template>
  <header class="rea-header" role="banner">
    <nav class="cmp-mainnavigation" id="mainnavigation">
      <input type="checkbox" id="toggle_mainnavigation" />
      <label for="toggle_mainnavigation" title="Toggle main navigation" class="is-site-name"
        >PopUpSim-ControlCenter.js</label
      >
      <ul>
        <li>
          <RouterLink to="/" class="elm-link" :title="$t('home')">
            {{ $t('home') }}
          </RouterLink>
        </li>
        <li>
          <RouterLink to="/user" class="elm-link" title="Benutzer">
            {{ $t('user') }}
          </RouterLink>
        </li>
        <li>
          <!-- Use a custom RouterLink here since db-ui highlights the nav item when aria-current="page" is set -->
          <!-- By default the RouterLink sets aria-current="page" only when exact route matches.  -->
          <!-- We want to highlight it also, when sub-routes (e.g /demo/quotes or /demo/quotes/create) is opened  -->
          <RouterLink custom v-slot="{ isActive, href, navigate }" to="/demo">
            <a
              :href="href"
              :aria-current="isActive ? 'page' : undefined"
              class="elm-link"
              title="Demo"
              @click="navigate"
              >{{ $t('demo') }}</a
            >
          </RouterLink>
        </li>
      </ul>
    </nav>
    <div class="cmp-brand">
      <RouterLink to="/" :title="$t('home')" rel="home">
        <img
          src="../assets/db_logo.svg"
          alt="Deutsche Bahn Logo"
          width=""
          height=""
          class="elm-image is-logo"
          elementtiming="logo"
        />
      </RouterLink>
      <span class="is-site-name">PopUpSim-ControlCenter.js</span>
    </div>
    <div class="rea-meta">
      <ul class="cmp-metanavigation">
        <li>
          <a
            v-if="!isAuthenticated"
            id="login"
            class="elm-link"
            :title="$t('signin')"
            rel="account"
            href="#"
            @click="login()"
          >
            {{ $t('signin') }}
          </a>
          <a
            v-else
            id="logout"
            class="elm-link"
            :title="$t('signout')"
            rel="account"
            href="#"
            @click="logout()"
          >
            {{ $t('signout') }}
          </a>
        </li>
      </ul>
      <ul class="cmp-language-switcher" aria-label="Select the language">
        <li :aria-current="locale === 'en' ? 'page' : undefined">
          <a
            @click="locale = 'en'"
            class="elm-link"
            title="English language"
            rel="alternate"
            href="#"
            hreflang="en"
            >EN</a
          >
        </li>
        <li :aria-current="locale === 'de' ? 'page' : undefined">
          <a
            @click="locale = 'de'"
            class="elm-link"
            title="Deutsche Sprache"
            rel="alternate"
            href="#"
            hreflang="de"
            >DE</a
          >
        </li>
      </ul>
    </div>
  </header>
</template>
