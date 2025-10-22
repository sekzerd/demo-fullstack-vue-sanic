import { createApp } from 'vue'
import '@/styles/tailwind.css'
import App from '@/App.vue'
import { router } from '@/routers/router.ts'

const app = createApp(App);

app.use(router)

app.mount('#app')
