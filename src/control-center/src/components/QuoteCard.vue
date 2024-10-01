<script setup lang="ts">
import type { Quote } from '@/utils/api'

defineProps<{
  quote: Quote
}>()
</script>

<template>
  <div class="cmp-card quote-card">
    <h2 class="elm-headline">{{ quote.title }}</h2>
    <p>
      {{ quote.body }}
    </p>
    <div class="btn-group">
      <RouterLink
        :to="{ name: 'quote', params: { slug: quote.slug } }"
        class="elm-button"
        data-variant="secondary-outline"
        data-size="small"
        type="button"
        data-icon-after="arrow-forward"
      >
        {{ $t('show') }}
      </RouterLink>
      <RouterLink
        :to="{ name: 'editQuote', params: { slug: quote.slug } }"
        class="elm-button is-icon-text-replace"
        data-variant="tertiary-plain"
        data-size="small"
        type="button"
        data-icon-after="edit"
      >
        {{ $t('edit') }}
      </RouterLink>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.quote-card {
  padding: 1rem;

  .elm-headline {
    margin-top: 0;
  }

  .btn-group {
    justify-content: space-between;
  }
}
</style>
