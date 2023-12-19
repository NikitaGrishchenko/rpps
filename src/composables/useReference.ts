import { useApi } from 'src/composables/useApi'
import { references, IReference } from 'src/types/reference'
import { onMounted, ref } from 'vue'

export function useReference(queries: string[]) {
  const { inProcess, fetch } = useApi()

  const reference = ref<IReference>({})

  onMounted(async () => {
    const data = await Promise.all(
      queries.map((query) =>
        fetch<references>({
          method: 'GET',
          url: `reference/${query}/`
        })
      )
    )
    for (let i = 0; i < queries.length; i++)
      reference.value[queries[i]] = data[i]
  })
  return {
    inProcess,
    reference
  }
}
