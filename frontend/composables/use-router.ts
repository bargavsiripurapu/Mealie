import { useRoute, WritableComputedRef, computed, nextTick, useRouter } from "@nuxtjs/composition-api";

export function useRouterQuery(query: string) {
  const router = useRoute();
  // TODO FUTURE: Remove when migrating to Vue 3

  const param: WritableComputedRef<string> = computed({
    get(): string {
      console.log("Get Query Change");
      // @ts-ignore For some reason, this could also return an array
      return router.value?.query[query] || "";
    },
    set(v: string): void {
      router.value.query[query] = v;
    },
  });

  return param;
}

export function useRouteQuery<T extends string | string[]>(name: string, defaultValue?: T) {
  const route = useRoute();
  const router = useRouter();

  return computed<any>({
    get() {
      const data = route.value.query[name];
      if (data == null) return defaultValue ?? null;
      return data;
    },
    set(v) {
      nextTick(() => {
        router.replace({ query: { ...route.value.query, [name]: v } });
      });
    },
  });
}
