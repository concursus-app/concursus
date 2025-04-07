import type { PageServerLoad, Actions } from './$types';

export const load: PageServerLoad = async ({ cookies }) => {
  return {
    name: "skibidi"
  };
}

export const actions = {
  default: async ({ cookies, request }) => {
    cookies.set('sessionID', 'skbiidi', { path: '/' });

    return { success: true };
  }
} satisfies Actions;
