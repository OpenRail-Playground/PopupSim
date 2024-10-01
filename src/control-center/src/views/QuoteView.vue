<script setup lang="ts">
import TheModal from '@/components/TheModal.vue'
import type { Quote } from '@/utils/api'
import { useQuotesStore } from '@/stores/quotes'
import { onBeforeMount, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const { getQuote, deleteQuote } = useQuotesStore()

const quote = ref<Quote>()
const showDeleteModal = ref(false)

onBeforeMount(() => {
  const slug = route.params?.slug
  quote.value = getQuote(Array.isArray(slug) ? slug[0] : slug)
})

async function removeQuote(slug: string) {
  await deleteQuote(slug)
  closeModal()
  router.push({ name: 'quotes' })
}

function closeModal() {
  showDeleteModal.value = false
}
</script>

<template>
  <div class="rea-main" v-if="quote">
    <h1 class="elm-headline">{{ $t('quote') }}</h1>
    <p>{{ quote.body }}</p>
    <p>
      {{ quote.author }}, {{ quote.createdAt
      }}<span v-if="quote.updatedAt && quote.updatedAt !== quote.createdAt">
        ({{ $t('refreshed') }}: {{ quote.updatedAt }})</span
      >
    </p>
    <div v-if="quote.notes">
      <h2>{{ $t('notes') }}</h2>
      <p>{{ quote.notes }}</p>
    </div>

    <div class="btn-group">
      <RouterLink
        :to="{ name: 'quotes' }"
        class="elm-button"
        data-variant="secondary-outline"
        data-size="small"
        type="button"
        data-icon="arrow-back"
      >
        {{ $t('back') }}
      </RouterLink>
      <RouterLink
        :to="{ name: 'editQuote', params: { slug: quote.slug } }"
        class="elm-button"
        data-variant="primary"
        data-size="small"
        type="button"
        data-icon-after="edit"
      >
        {{ $t('edit') }}
      </RouterLink>
      <button
        @click="showDeleteModal = true"
        class="elm-button"
        data-variant="primary"
        type="button"
        data-icon-after="delete"
      >
        {{ $t('delete') }}
      </button>
      <TheModal
        :title="$t('deleteQuoteTitle')"
        :ok-label="$t('yes')"
        :show="showDeleteModal"
        @ok="removeQuote(quote.slug)"
        @close="closeModal()"
      >
        {{ $t('deleteQuoteBody') }}
      </TheModal>
    </div>
  </div>
</template>
