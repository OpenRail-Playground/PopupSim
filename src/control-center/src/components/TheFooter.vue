<script setup lang="ts"></script>

<template>
  <footer class="rea-footer" role="contentinfo">
    <ul class="cmp-metanavigation">
      <li>
        <RouterLink to="/imprint" class="elm-link" :title="$t('imprint')">
          {{ $t('imprint') }}
        </RouterLink>
      </li>
      <li>
        <RouterLink to="/help" class="elm-link" :title="$t('help')">
          {{ $t('help') }}
        </RouterLink>
      </li>
    </ul>
    Copyright 2024
  </footer>
</template>

<style lang="scss" scoped>
footer.rea-footer {
  position: sticky;
}
</style>
