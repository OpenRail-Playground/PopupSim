<script setup lang="ts">
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()
</script>

<template>
  <header class="rea-header" role="banner">
    <nav class="cmp-mainnavigation" id="mainnavigation">
      <input type="checkbox" id="toggle_mainnavigation" />
      <label for="toggle_mainnavigation" title="Toggle main navigation" class="is-site-name"
        >PopUpSim - ControlCenter</label
      >
      <ul>
        <li>
          <RouterLink to="/" class="elm-link" :title="$t('home')">
            {{ $t('home') }}
          </RouterLink>
        </li>
        <li>
          <RouterLink to="/visualizer" class="elm-link" :title="$t('visualizer')">
            {{ $t('visualizer') }}
          </RouterLink>
        </li>
      </ul>
    </nav>
    <div class="cmp-brand">
      <RouterLink to="/" :title="$t('home')" rel="home">
        <img
          src="../assets/3LH.png"
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
