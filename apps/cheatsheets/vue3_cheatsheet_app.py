import streamlit as st

# 基础部分
st.header("Vue 3 基础")

basic_col1, basic_col2 = st.columns(2)

with basic_col1:
    with st.expander("创建 Vue 应用", expanded=True):
        st.code("""
        // 创建应用实例
        import { createApp } from 'vue'
        import App from './App.vue'

        const app = createApp(App)
        app.mount('#app')

        // App.vue - 组件基础结构
        <template>
          <div class="app">
            <h1>{{ title }}</h1>
            <button @click="increment">Count: {{ count }}</button>
          </div>
        </template>

        <script setup>
        import { ref } from 'vue'

        // 响应式数据
        const title = ref('Hello Vue 3')
        const count = ref(0)

        // 方法
        const increment = () => {
          count.value++
        }
        </script>

        <style scoped>
        .app {
          text-align: center;
          padding: 20px;
        }
        </style>
        """, language="html")

with basic_col2:
    with st.expander("组合式 API 基础", expanded=True):
        st.code("""
        <script setup>
        import { ref, reactive, computed, onMounted } from 'vue'

        // ref: 基础类型的响应式
        const message = ref('Hello')
        console.log(message.value) // 访问值需要 .value

        // reactive: 对象的响应式
        const state = reactive({
          count: 0,
          user: {
            name: 'John',
            age: 25
          }
        })

        // computed: 计算属性
        const doubleCount = computed(() => state.count * 2)

        // 方法
        const updateMessage = () => {
          message.value = 'Updated'
          state.count++
        }

        // 生命周期钩子
        onMounted(() => {
          console.log('组件已挂载')
        })
        </script>

        <template>
          <div>
            <p>{{ message }}</p>
            <p>Count: {{ state.count }}</p>
            <p>Double: {{ doubleCount }}</p>
            <p>User: {{ state.user.name }}</p>
            <button @click="updateMessage">Update</button>
          </div>
        </template>
        """, language="html")

# 响应式系统
st.header("响应式系统")

reactive_col1, reactive_col2 = st.columns(2)

with reactive_col1:
    with st.expander("ref vs reactive", expanded=True):
        st.code("""
        <script setup>
        import { ref, reactive, toRef, toRefs } from 'vue'

        // ref - 适用于基础类型
        const count = ref(0)
        const message = ref('Hello')
        
        // reactive - 适用于对象
        const state = reactive({
          user: {
            name: 'John',
            age: 25
          },
          settings: {
            theme: 'dark'
          }
        })

        // toRef - 创建对象属性的ref
        const name = toRef(state.user, 'name')

        // toRefs - 将响应式对象转换为普通对象，其中每个属性都是ref
        const { theme } = toRefs(state.settings)

        // 修改值
        const updateValues = () => {
          count.value++ // ref 需要 .value
          state.user.name = 'Jane' // reactive 直接修改
          name.value = 'Mike' // 通过 ref 修改也会更新原对象
          theme.value = 'light' // 解构的 ref 也需要 .value
        }
        </script>

        <template>
          <div>
            <p>Count: {{ count }}</p>
            <p>Name: {{ state.user.name }}</p>
            <p>Theme: {{ theme }}</p>
            <button @click="updateValues">Update</button>
          </div>
        </template>
        """, language="html")

with reactive_col2:
    with st.expander("响应式工具函数", expanded=True):
        st.code("""
        <script setup>
        import { 
          ref, 
          computed, 
          watch, 
          watchEffect,
          readonly,
          isRef,
          unref,
          isProxy,
          isReactive
        } from 'vue'

        const count = ref(0)
        const user = reactive({
          name: 'John',
          age: 25
        })

        // computed - 计算属性
        const doubleCount = computed(() => count.value * 2)
        const fullName = computed({
          get: () => user.name + ' Doe',
          set: (val) => user.name = val.split(' ')[0]
        })

        // watch - 侦听特定数据源
        watch(count, (newVal, oldVal) => {
          console.log(`Count changed: ${oldVal} -> ${newVal}`)
        })

        // watchEffect - 自动收集依赖并侦听
        watchEffect(() => {
          console.log(`Count is: ${count.value}`)
          console.log(`Name is: ${user.name}`)
        })

        // readonly - 创建只读代理
        const readOnlyUser = readonly(user)

        // 工具函数
        console.log(isRef(count)) // true
        console.log(unref(count)) // 获取值
        console.log(isProxy(user)) // true
        console.log(isReactive(user)) // true

        // 停止侦听
        const stop = watchEffect(() => {})
        // 在需要时停止
        // stop()
        </script>
        """, language="html")

# 生命周期钩子
st.header("生命周期钩子")

lifecycle_col1, lifecycle_col2 = st.columns(2)

with lifecycle_col1:
    with st.expander("组合式 API 生命周期", expanded=True):
        st.code("""
        <script setup>
        import {
          onBeforeMount,
          onMounted,
          onBeforeUpdate,
          onUpdated,
          onBeforeUnmount,
          onUnmounted,
          onErrorCaptured,
          onActivated,
          onDeactivated
        } from 'vue'

        // 在组件挂载前
        onBeforeMount(() => {
          console.log('组件挂载前')
        })

        // 组件挂载后
        onMounted(() => {
          console.log('组件已挂载')
          // 可以访问 DOM
          // 适合初始化或获取数据
        })

        // 数据更新前
        onBeforeUpdate(() => {
          console.log('数据更新前')
        })

        // 数据更新后
        onUpdated(() => {
          console.log('数据已更新')
        })

        // 组件卸载前
        onBeforeUnmount(() => {
          console.log('组件卸载前')
          // 清理副作用
        })

        // 组件卸载后
        onUnmounted(() => {
          console.log('组件已卸载')
        })

        // 错误捕获
        onErrorCaptured((err, instance, info) => {
          console.error('捕获到错误:', err)
          return false // 阻止错误继续传播
        })

        // keep-alive 组件激活时
        onActivated(() => {
          console.log('组件被激活')
        })

        // keep-alive 组件停用时
        onDeactivated(() => {
          console.log('组件被停用')
        })
        </script>
        """, language="html")

with lifecycle_col2:
    with st.expander("实践示例", expanded=True):
        st.code("""
        <script setup>
        import { ref, onMounted, onUnmounted } from 'vue'

        const data = ref(null)
        const timer = ref(null)

        // 加载数据
        const fetchData = async () => {
          try {
            const response = await fetch('https://api.example.com/data')
            data.value = await response.json()
          } catch (error) {
            console.error('Failed to fetch data:', error)
          }
        }

        // 定时器
        const startTimer = () => {
          timer.value = setInterval(() => {
            console.log('Timer tick')
          }, 1000)
        }

        // 组件挂载后
        onMounted(() => {
          // 加载初始数据
          fetchData()
          // 启动定时器
          startTimer()
          // 添加事件监听
          window.addEventListener('resize', handleResize)
        })

        // 组件卸载前清理
        onUnmounted(() => {
          // 清理定时器
          if (timer.value) {
            clearInterval(timer.value)
          }
          // 移除事件监听
          window.removeEventListener('resize', handleResize)
        })

        // 事件处理
        const handleResize = () => {
          console.log('Window resized')
        }
        </script>

        <template>
          <div>
            <div v-if="data">
              {{ data }}
            </div>
            <div v-else>
              Loading...
            </div>
          </div>
        </template>
        """, language="html")



# 组件通信
st.header("组件通信")

comm_col1, comm_col2 = st.columns(2)

with comm_col1:
    with st.expander("Props 和 Emits", expanded=True):
        st.code("""
        // 子组件 ChildComponent.vue
        <script setup>
        // Props 定义
        const props = defineProps({
          title: {
            type: String,
            required: true
          },
          count: {
            type: Number,
            default: 0
          },
          user: {
            type: Object,
            default: () => ({
              name: 'Guest',
              role: 'user'
            })
          }
        })

        // Emits 定义
        const emit = defineEmits(['update', 'delete'])

        // 触发事件
        const handleClick = () => {
          emit('update', {
            id: 1,
            value: 'new value'
          })
        }

        // 使用 v-model
        const modelValue = defineModel()
        // 或者带修饰符
        const [modelValue, modelModifiers] = defineModel()
        </script>

        <template>
          <div>
            <h2>{{ title }}</h2>
            <p>Count: {{ count }}</p>
            <p>User: {{ user.name }}</p>
            <button @click="handleClick">Update</button>
            <input v-model="modelValue" />
          </div>
        </template>

        // 父组件使用
        <template>
          <ChildComponent
            title="My Title"
            :count="count"
            :user="user"
            @update="handleUpdate"
            v-model="value"
          />
        </template>
        """, language="html")

with comm_col2:
    with st.expander("依赖注入", expanded=True):
        st.code("""
        // 父组件提供数据
        <script setup>
        import { provide, ref, readonly } from 'vue'

        // 提供响应式数据
        const theme = ref('light')
        const updateTheme = (newTheme) => {
          theme.value = newTheme
        }

        // 提供只读数据防止子组件修改
        provide('theme', readonly(theme))
        provide('updateTheme', updateTheme)

        // 提供符号键避免命名冲突
        const themeSymbol = Symbol()
        provide(themeSymbol, theme)

        // 提供对象
        provide('settings', {
          api: 'https://api.example.com',
          timeout: 5000
        })
        </script>

        // 子组件注入数据
        <script setup>
        import { inject } from 'vue'

        // 基础注入
        const theme = inject('theme')
        const updateTheme = inject('updateTheme')

        // 带默认值的注入
        const settings = inject('settings', {
          api: 'default-api',
          timeout: 3000
        })

        // 使用符号键注入
        const theme2 = inject(themeSymbol)

        // 注入函数
        const updateTheme2 = inject('updateTheme', (theme) => {
          console.warn('updateTheme not provided')
        })
        </script>

        <template>
          <div :class="theme">
            <button @click="updateTheme('dark')">
              Toggle Theme
            </button>
            <p>API: {{ settings.api }}</p>
          </div>
        </template>
        """, language="html")

# 事件总线
event_col1, event_col2 = st.columns(2)

with event_col1:
    with st.expander("事件总线", expanded=True):
        st.code("""
        // eventBus.js
        import mitt from 'mitt'

        export const eventBus = mitt()

        // 组件 A
        <script setup>
        import { eventBus } from './eventBus'

        // 发送事件
        const sendMessage = () => {
          eventBus.emit('message', {
            text: 'Hello from Component A',
            timestamp: Date.now()
          })
        }

        // 清理事件监听
        onUnmounted(() => {
          eventBus.all.clear()
        })
        </script>

        // 组件 B
        <script setup>
        import { eventBus } from './eventBus'
        import { onMounted, onUnmounted } from 'vue'

        // 监听事件
        const handleMessage = (event) => {
          console.log('Received:', event)
        }

        onMounted(() => {
          eventBus.on('message', handleMessage)
        })

        onUnmounted(() => {
          eventBus.off('message', handleMessage)
        })
        </script>
        """, language="html")

with event_col2:
    with st.expander("跨组件通信最佳实践", expanded=True):
        st.code("""
        // 状态管理 store/message.js
        import { ref, readonly } from 'vue'

        const messages = ref([])

        export function useMessages() {
          const addMessage = (message) => {
            messages.value.push({
              id: Date.now(),
              text: message,
              timestamp: new Date()
            })
          }

          const removeMessage = (id) => {
            const index = messages.value.findIndex(m => m.id === id)
            if (index > -1) {
              messages.value.splice(index, 1)
            }
          }

          return {
            messages: readonly(messages),
            addMessage,
            removeMessage
          }
        }

        // 组件中使用
        <script setup>
        import { useMessages } from '@/store/message'

        const { messages, addMessage, removeMessage } = useMessages()

        // 发送消息
        const sendMessage = () => {
          addMessage('Hello World')
        }

        // 删除消息
        const deleteMessage = (id) => {
          removeMessage(id)
        }
        </script>

        <template>
          <div>
            <button @click="sendMessage">Send Message</button>
            <ul>
              <li v-for="msg in messages" :key="msg.id">
                {{ msg.text }}
                <button @click="deleteMessage(msg.id)">
                  Delete
                </button>
              </li>
            </ul>
          </div>
        </template>
        """, language="html")
        
        
 
# 组合式函数
st.header("组合式函数（Composables）")

composable_col1, composable_col2 = st.columns(2)

with composable_col1:
    with st.expander("基础 Composables", expanded=True):
        st.code("""
        // composables/useCounter.js
        import { ref, computed } from 'vue'

        export function useCounter(initialValue = 0) {
          const count = ref(initialValue)
          const doubleCount = computed(() => count.value * 2)

          const increment = () => count.value++
          const decrement = () => count.value--
          const reset = () => count.value = initialValue

          return {
            count,
            doubleCount,
            increment,
            decrement,
            reset
          }
        }

        // composables/useFetch.js
        import { ref, shallowRef } from 'vue'

        export function useFetch(options = {}) {
          const data = shallowRef(null)
          const error = ref(null)
          const loading = ref(false)

          const execute = async (url, config = {}) => {
            loading.value = true
            error.value = null
            
            try {
              const response = await fetch(url, {
                ...options,
                ...config
              })
              
              if (!response.ok) {
                throw new Error(response.statusText)
              }
              
              data.value = await response.json()
            } catch (err) {
              error.value = err
            } finally {
              loading.value = false
            }
          }

          return {
            data,
            error,
            loading,
            execute
          }
        }

        // 使用示例
        <script setup>
        import { useCounter } from '@/composables/useCounter'
        import { useFetch } from '@/composables/useFetch'

        const { count, increment } = useCounter(10)
        const { data, loading, execute } = useFetch()

        // 加载数据
        execute('https://api.example.com/data')
        </script>
        """, language="javascript")

with composable_col2:
    with st.expander("进阶 Composables", expanded=True):
        st.code("""
        // composables/useStorage.js
        import { ref, watch } from 'vue'

        export function useStorage(key, defaultValue) {
          // 创建响应式数据
          const storedValue = ref(defaultValue)

          // 尝试从 localStorage 获取数据
          try {
            const value = window.localStorage.getItem(key)
            if (value) {
              storedValue.value = JSON.parse(value)
            }
          } catch (err) {
            console.warn(`Error reading localStorage key "${key}":`, err)
          }

          // 监听变化并更新 localStorage
          watch(
            storedValue,
            (newValue) => {
              try {
                window.localStorage.setItem(key, JSON.stringify(newValue))
              } catch (err) {
                console.warn(`Error setting localStorage key "${key}":`, err)
              }
            },
            { deep: true }
          )

          return storedValue
        }

        // composables/useAsync.js
        import { ref, computed } from 'vue'

        export function useAsync(asyncFunction) {
          const data = ref(null)
          const error = ref(null)
          const loading = ref(false)
          const loaded = ref(false)

          const execute = async (...args) => {
            loading.value = true
            error.value = null
            
            try {
              data.value = await asyncFunction(...args)
            } catch (err) {
              error.value = err
            } finally {
              loading.value = false
              loaded.value = true
            }
          }

          const status = computed(() => {
            if (loading.value) return 'loading'
            if (error.value) return 'error'
            if (loaded.value) return 'loaded'
            return 'idle'
          })

          return {
            data,
            error,
            loading,
            loaded,
            status,
            execute
          }
        }

        // 使用示例
        <script setup>
        import { useStorage } from '@/composables/useStorage'
        import { useAsync } from '@/composables/useAsync'

        // 持久化状态
        const theme = useStorage('theme', 'light')

        // 异步操作
        const fetchUser = async (id) => {
          const response = await fetch(`/api/users/${id}`)
          return response.json()
        }

        const {
          data: user,
          status,
          execute: loadUser
        } = useAsync(fetchUser)

        // 加载用户数据
        loadUser(1)
        </script>

        <template>
          <div :class="theme">
            <div v-if="status === 'loading'">Loading...</div>
            <div v-else-if="status === 'error'">Error!</div>
            <div v-else-if="status === 'loaded'">
              {{ user }}
            </div>
          </div>
        </template>
        """, language="javascript")

# 实用 Composables
util_col1, util_col2 = st.columns(2)

with util_col1:
    with st.expander("DOM 相关", expanded=True):
        st.code("""
        // composables/useEventListener.js
        import { onMounted, onUnmounted } from 'vue'

        export function useEventListener(target, event, callback) {
          onMounted(() => {
            target.addEventListener(event, callback)
          })

          onUnmounted(() => {
            target.removeEventListener(event, callback)
          })
        }

        // composables/useIntersectionObserver.js
        import { ref, onUnmounted } from 'vue'

        export function useIntersectionObserver(
          options = {}
        ) {
          const isIntersecting = ref(false)
          const element = ref(null)

          const observer = new IntersectionObserver(([entry]) => {
            isIntersecting.value = entry.isIntersecting
          }, options)

          const observe = (el) => {
            element.value = el
            if (el) {
              observer.observe(el)
            }
          }

          onUnmounted(() => {
            if (element.value) {
              observer.unobserve(element.value)
            }
          })

          return {
            isIntersecting,
            observe
          }
        }

        // 使用示例
        <script setup>
        import { ref } from 'vue'
        import { useEventListener } from '@/composables/useEventListener'
        import { useIntersectionObserver } from '@/composables/useIntersectionObserver'

        // 事件监听
        useEventListener(window, 'resize', () => {
          console.log('window resized')
        })

        // 交叉观察
        const { isIntersecting, observe } = useIntersectionObserver({
          threshold: 0.5
        })
        </script>

        <template>
          <div ref="observe">
            <div v-if="isIntersecting">
              Element is visible!
            </div>
          </div>
        </template>
        """, language="javascript")

with util_col2:
    with st.expander("状态相关", expanded=True):
        st.code("""
        // composables/useDebounce.js
        import { customRef } from 'vue'

        export function useDebounce(value, delay = 200) {
          return customRef((track, trigger) => {
            let timeout
            return {
              get() {
                track()
                return value
              },
              set(newValue) {
                clearTimeout(timeout)
                timeout = setTimeout(() => {
                  value = newValue
                  trigger()
                }, delay)
              }
            }
          })
        }

        // composables/useValidation.js
        import { reactive, computed } from 'vue'

        export function useValidation(rules) {
          const errors = reactive({})
          const isValid = computed(() => 
            Object.keys(errors).length === 0
          )

          const validate = (data) => {
            Object.keys(rules).forEach(key => {
              const value = data[key]
              const validations = rules[key]

              errors[key] = validations
                .map(validation => validation(value))
                .filter(error => error !== true)
            })

            return isValid.value
          }

          return {
            errors,
            isValid,
            validate
          }
        }

        // 使用示例
        <script setup>
        import { ref } from 'vue'
        import { useDebounce } from '@/composables/useDebounce'
        import { useValidation } from '@/composables/useValidation'

        // 防抖搜索
        const searchQuery = useDebounce('', 300)

        // 表单验证
        const rules = {
          email: [
            v => !!v || '邮箱是必填的',
            v => /.+@.+/.test(v) || '邮箱格式不正确'
          ],
          password: [
            v => !!v || '密码是必填的',
            v => v.length >= 6 || '密码至少6个字符'
          ]
        }

        const { errors, isValid, validate } = useValidation(rules)

        const formData = reactive({
          email: '',
          password: ''
        })

        const handleSubmit = () => {
          if (validate(formData)) {
            // 提交表单
          }
        }
        </script>
        """, language="javascript")
        

# 路由
st.header("Vue Router")

router_col1, router_col2 = st.columns(2)

with router_col1:
    with st.expander("路由配置", expanded=True):
        st.code("""
        // router/index.js
        import { createRouter, createWebHistory } from 'vue-router'

        const router = createRouter({
          history: createWebHistory(),
          routes: [
            {
              path: '/',
              name: 'Home',
              component: () => import('@/views/Home.vue'),
              meta: {
                title: '首页',
                requiresAuth: true
              }
            },
            {
              path: '/user/:id',
              name: 'UserProfile',
              component: () => import('@/views/UserProfile.vue'),
              props: true, // 将路由参数作为组件的 props
              children: [
                {
                  path: 'posts',
                  name: 'UserPosts',
                  component: () => import('@/views/UserPosts.vue')
                }
              ]
            },
            {
              path: '/:pathMatch(.*)*',
              name: 'NotFound',
              component: () => import('@/views/NotFound.vue')
            }
          ]
        })

        // 全局前置守卫
        router.beforeEach((to, from, next) => {
          // 设置页面标题
          document.title = to.meta.title || 'Default Title'

          // 检查认证
          if (to.meta.requiresAuth && !isAuthenticated()) {
            next({ name: 'Login' })
          } else {
            next()
          }
        })

        export default router
        """, language="javascript")

with router_col2:
    with st.expander("路由使用", expanded=True):
        st.code("""
        <script setup>
        import { useRouter, useRoute } from 'vue-router'

        const router = useRouter()
        const route = useRoute()

        // 编程式导航
        const navigate = () => {
          router.push({
            name: 'UserProfile',
            params: { id: 1 },
            query: { tab: 'posts' }
          })
        }

        // 获取路由参数
        const userId = route.params.id
        const currentTab = route.query.tab

        // 路由操作
        const goBack = () => router.back()
        const goForward = () => router.forward()
        const refreshPage = () => router.go(0)

        // 路由守卫
        onBeforeRouteLeave((to, from) => {
          const answer = window.confirm('确定要离开吗？')
          if (!answer) return false
        })

        onBeforeRouteUpdate((to, from) => {
          // 路由参数改变时的处理
        })
        </script>

        <template>
          <nav>
            <router-link :to="{ name: 'Home' }">首页</router-link>
            <router-link 
              :to="{ name: 'UserProfile', params: { id: userId }}"
              active-class="active"
            >
              用户资料
            </router-link>
          </nav>

          <router-view v-slot="{ Component }">
            <transition name="fade" mode="out-in">
              <component :is="Component" />
            </transition>
          </router-view>
        </template>
        """, language="html")

# 状态管理
st.header("Pinia 状态管理")

store_col1, store_col2 = st.columns(2)

with store_col1:
    with st.expander("Store 定义", expanded=True):
        st.code("""
        // stores/user.js
        import { defineStore } from 'pinia'
        import { ref, computed } from 'vue'

        export const useUserStore = defineStore('user', () => {
          // 状态
          const user = ref(null)
          const token = ref(null)
          const loading = ref(false)

          // Getters
          const isLoggedIn = computed(() => !!token.value)
          const fullName = computed(() => {
            if (!user.value) return ''
            return `${user.value.firstName} ${user.value.lastName}`
          })

          // Actions
          async function login(credentials) {
            loading.value = true
            try {
              const response = await api.login(credentials)
              user.value = response.user
              token.value = response.token
            } catch (error) {
              throw new Error('Login failed')
            } finally {
              loading.value = false
            }
          }

          function logout() {
            user.value = null
            token.value = null
          }

          return {
            // 状态
            user,
            token,
            loading,
            // Getters
            isLoggedIn,
            fullName,
            // Actions
            login,
            logout
          }
        })

        // stores/cart.js
        export const useCartStore = defineStore('cart', {
          state: () => ({
            items: [],
            loading: false
          }),
          
          getters: {
            totalItems: (state) => state.items.length,
            totalAmount: (state) => 
              state.items.reduce((sum, item) => 
                sum + item.price * item.quantity, 0
              )
          },
          
          actions: {
            addItem(product) {
              const existingItem = this.items.find(
                item => item.id === product.id
              )
              
              if (existingItem) {
                existingItem.quantity++
              } else {
                this.items.push({
                  ...product,
                  quantity: 1
                })
              }
            },
            
            removeItem(productId) {
              const index = this.items.findIndex(
                item => item.id === productId
              )
              if (index > -1) {
                this.items.splice(index, 1)
              }
            },
            
            clearCart() {
              this.items = []
            }
          }
        })
        """, language="javascript")

with store_col2:
    with st.expander("Store 使用", expanded=True):
        st.code("""
        <script setup>
        import { storeToRefs } from 'pinia'
        import { useUserStore } from '@/stores/user'
        import { useCartStore } from '@/stores/cart'

        // 用户 Store
        const userStore = useUserStore()
        // 解构时保持响应性
        const { user, isLoggedIn, fullName } = storeToRefs(userStore)
        // Actions 可以直接解构
        const { login, logout } = userStore

        // 购物车 Store
        const cartStore = useCartStore()
        const { items, totalItems, totalAmount } = storeToRefs(cartStore)

        // 登录处理
        const handleLogin = async () => {
          try {
            await login({
              username: 'user',
              password: 'pass'
            })
            // 登录成功
          } catch (error) {
            // 错误处理
          }
        }

        // 购物车操作
        const addToCart = (product) => {
          cartStore.addItem(product)
        }

        // 批量操作
        const checkout = () => {
          cartStore.$patch((state) => {
            state.items = []
            state.loading = false
          })
        }

        // 订阅 store 变化
        cartStore.$subscribe((mutation, state) => {
          // 持久化到本地存储
          localStorage.setItem('cart', JSON.stringify(state))
        })
        </script>

        <template>
          <div>
            <div v-if="isLoggedIn">
              <h1>Welcome, {{ fullName }}</h1>
              <button @click="logout">Logout</button>
            </div>

            <div class="cart">
              <h2>购物车 ({{ totalItems }})</h2>
              <ul>
                <li v-for="item in items" :key="item.id">
                  {{ item.name }} - ¥{{ item.price }}
                  x {{ item.quantity }}
                  <button @click="cartStore.removeItem(item.id)">
                    删除
                  </button>
                </li>
              </ul>
              <p>总计: ¥{{ totalAmount }}</p>
              <button @click="cartStore.clearCart">
                清空购物车
              </button>
            </div>
          </div>
        </template>
        """, language="html")
        

# 自定义指令
st.header("自定义指令")

directive_col1, directive_col2 = st.columns(2)

with directive_col1:
    with st.expander("基础指令", expanded=True):
        st.code("""
        // directives/focus.js
        export const vFocus = {
          mounted: (el) => el.focus()
        }

        // directives/click-outside.js
        export const vClickOutside = {
          mounted(el, binding) {
            el._clickOutside = (event) => {
              if (!(el === event.target || el.contains(event.target))) {
                binding.value(event)
              }
            }
            document.addEventListener('click', el._clickOutside)
          },
          unmounted(el) {
            document.removeEventListener('click', el._clickOutside)
          }
        }

        // 全局注册
        app.directive('focus', vFocus)
        app.directive('click-outside', vClickOutside)

        // 使用示例
        <template>
          <input v-focus />
          <div v-click-outside="onClickOutside">
            点击外部关闭
          </div>
        </template>
        """, language="javascript")

with directive_col2:
    with st.expander("高级指令", expanded=True):
        st.code("""
        // directives/intersection.js
        export const vIntersection = {
          mounted(el, binding) {
            const options = {
              root: binding.arg === 'parent' ? el.parentElement : null,
              ...binding.modifiers,
              threshold: binding.value?.threshold || 0
            }

            const observer = new IntersectionObserver(([entry]) => {
              if (typeof binding.value === 'function') {
                binding.value(entry.isIntersecting)
              } else if (binding.value?.handler) {
                binding.value.handler(entry.isIntersecting)
              }
            }, options)

            el._observer = observer
            observer.observe(el)
          },
          unmounted(el) {
            el._observer?.disconnect()
          }
        }

        // directives/resize.js
        export const vResize = {
          mounted(el, binding) {
            const options = binding.value || {}
            
            el._resizeObserver = new ResizeObserver(entries => {
              for (const entry of entries) {
                const { width, height } = entry.contentRect
                if (typeof options.onResize === 'function') {
                  options.onResize({ width, height })
                }
              }
            })
            
            el._resizeObserver.observe(el)
          },
          unmounted(el) {
            el._resizeObserver?.disconnect()
          }
        }

        // 使用示例
        <template>
          <div v-intersection="onIntersect">
            进入视口时触发
          </div>
          
          <div v-intersection="{
            threshold: 0.5,
            handler: onIntersect
          }">
            自定义配置
          </div>

          <div v-resize="{
            onResize: ({ width, height }) => {
              console.log('Element resized:', width, height)
            }
          }">
            监听大小变化
          </div>
        </template>
        """, language="javascript")

# 插件系统
st.header("插件系统")

plugin_col1, plugin_col2 = st.columns(2)

with plugin_col1:
    with st.expander("插件开发", expanded=True):
        st.code("""
        // plugins/i18n.js
        export default {
          install: (app, options) => {
            // 注入全局属性
            app.config.globalProperties.$translate = (key) => {
              return options.messages[options.locale][key]
            }

            // 注入全局方法
            app.provide('i18n', {
              locale: options.locale,
              messages: options.messages,
              t: (key) => options.messages[options.locale][key]
            })

            // 添加全局指令
            app.directive('t', {
              mounted(el, binding) {
                el.textContent = options.messages[options.locale][binding.value]
              }
            })

            // 添加全局组件
            app.component('i18n-text', {
              props: {
                keyName: String
              },
              setup(props) {
                const i18n = inject('i18n')
                return () => h('span', {}, i18n.t(props.keyName))
              }
            })
          }
        }

        // 使用插件
        import i18nPlugin from './plugins/i18n'

        app.use(i18nPlugin, {
          locale: 'zh',
          messages: {
            zh: {
              hello: '你好',
              welcome: '欢迎'
            },
            en: {
              hello: 'Hello',
              welcome: 'Welcome'
            }
          }
        })
        """, language="javascript")

with plugin_col2:
    with st.expander("实用插件示例", expanded=True):
        st.code("""
        // plugins/toast.js
        import { createVNode, render } from 'vue'
        import ToastComponent from './ToastComponent.vue'

        export default {
          install: (app) => {
            // 创建容器
            const container = document.createElement('div')
            document.body.appendChild(container)

            // 创建 toast 函数
            const toast = (message, options = {}) => {
              const vnode = createVNode(ToastComponent, {
                message,
                ...options,
                onDestroy: () => {
                  render(null, container)
                }
              })
              
              render(vnode, container)
            }

            // 添加到全局属性
            app.config.globalProperties.$toast = toast
            // 通过 provide/inject 使用
            app.provide('toast', toast)
          }
        }

        // plugins/auth.js
        export default {
          install: (app, options) => {
            const auth = {
              user: null,
              token: null,
              
              async login(credentials) {
                // 登录逻辑
                this.token = 'token'
                this.user = { id: 1, name: 'User' }
              },
              
              logout() {
                this.token = null
                this.user = null
              },
              
              isAuthenticated() {
                return !!this.token
              }
            }

            app.config.globalProperties.$auth = auth
            app.provide('auth', auth)

            // 添加全局导航守卫
            if (options?.router) {
              options.router.beforeEach((to, from, next) => {
                if (to.meta.requiresAuth && !auth.isAuthenticated()) {
                  next({ name: 'login' })
                } else {
                  next()
                }
              })
            }
          }
        }

        // 使用示例
        <script setup>
        import { inject } from 'vue'

        const toast = inject('toast')
        const auth = inject('auth')

        const showToast = () => {
          toast('操作成功！', {
            type: 'success',
            duration: 3000
          })
        }

        const login = async () => {
          await auth.login({
            username: 'user',
            password: 'pass'
          })
          toast('登录成功')
        }
        </script>
        """, language="javascript")


# 性能优化
st.header("性能优化")

perf_col1, perf_col2 = st.columns(2)

with perf_col1:
    with st.expander("组件优化", expanded=True):
        st.code("""
        // 动态组件导入
        <script setup>
        import { defineAsyncComponent } from 'vue'

        // 异步组件
        const AsyncComponent = defineAsyncComponent(() =>
          import('./components/HeavyComponent.vue')
        )

        // 带加载和错误状态的异步组件
        const AsyncComponentWithOptions = defineAsyncComponent({
          loader: () => import('./components/HeavyComponent.vue'),
          loadingComponent: LoadingSpinner,
          errorComponent: ErrorComponent,
          delay: 200,
          timeout: 3000
        })
        </script>

        // 组件缓存
        <template>
          <keep-alive :include="['ListComponent']" :max="10">
            <component :is="currentComponent" />
          </keep-alive>
        </template>

        // 虚拟列表
        <script setup>
        import { ref, computed } from 'vue'

        const items = ref([/* 大量数据 */])
        const itemHeight = 50
        const visibleItems = 10
        const scrollTop = ref(0)

        const visibleData = computed(() => {
          const start = Math.floor(scrollTop.value / itemHeight)
          const end = start + visibleItems
          return items.value.slice(start, end)
        })

        const containerStyle = computed(() => ({
          height: `${visibleItems * itemHeight}px`,
          overflow: 'auto'
        }))

        const contentStyle = computed(() => ({
          height: `${items.value.length * itemHeight}px`,
          position: 'relative'
        }))
        </script>

        <template>
          <div 
            :style="containerStyle"
            @scroll="scrollTop = $event.target.scrollTop"
          >
            <div :style="contentStyle">
              <div
                v-for="(item, index) in visibleData"
                :key="item.id"
                :style="{
                  position: 'absolute',
                  top: `${(index + Math.floor(scrollTop / itemHeight)) * itemHeight}px`,
                  height: `${itemHeight}px`
                }"
              >
                {{ item.content }}
              </div>
            </div>
          </div>
        </template>
        """, language="html")

with perf_col2:
    with st.expander("渲染优化", expanded=True):
        st.code("""
        // 大列表优化
        <script setup>
        import { shallowRef, nextTick } from 'vue'

        // 使用 shallowRef 避免深层响应
        const list = shallowRef([])

        // 批量更新
        const updateList = async (newItems) => {
          list.value = []
          await nextTick()
          list.value = newItems
        }
        </script>

        // 避免不必要的渲染
        <script setup>
        import { computed } from 'vue'

        // 使用计算属性缓存结果
        const filteredList = computed(() => {
          return expensiveFilter(props.list)
        })

        // 使用 v-once 处理静态内容
        const StaticComponent = {
          template: `
            <div v-once>
              <h1>{{ staticTitle }}</h1>
              <div>{{ staticContent }}</div>
            </div>
          `
        }
        </script>

        <template>
          <!-- 使用 v-memo 缓存条件渲染 -->
          <div v-memo="[item.id, item.selected]">
            {{ expensiveComputation(item) }}
          </div>

          <!-- 使用 v-show 代替频繁切换的 v-if -->
          <div v-show="isVisible">
            频繁切换的内容
          </div>
        </template>

        // 事件处理优化
        <script setup>
        import { onMounted, onUnmounted } from 'vue'

        // 事件委托
        const handleClick = (event) => {
          const button = event.target.closest('button')
          if (button) {
            const id = button.dataset.id
            // 处理点击
          }
        }

        onMounted(() => {
          document.addEventListener('click', handleClick)
        })

        onUnmounted(() => {
          document.removeEventListener('click', handleClick)
        })
        </script>

        <template>
          <div @click="handleClick">
            <button v-for="item in items" :key="item.id" :data-id="item.id">
              {{ item.name }}
            </button>
          </div>
        </template>
        """, language="html")

# 构建优化
build_col1, build_col2 = st.columns(2)

with build_col1:
    with st.expander("Vite 构建优化", expanded=True):
        st.code("""
        // vite.config.js
        import { defineConfig } from 'vite'
        import vue from '@vitejs/plugin-vue'
        import { visualizer } from 'rollup-plugin-visualizer'

        export default defineConfig({
          plugins: [
            vue(),
            visualizer({
              open: true,
              gzipSize: true,
              brotliSize: true
            })
          ],
          
          build: {
            // 代码分割
            rollupOptions: {
              output: {
                manualChunks: {
                  'vendor': ['vue', 'vue-router', 'pinia'],
                  'utils': ['./src/utils'],
                  'components': ['./src/components']
                }
              }
            },
            
            // 压缩选项
            minify: 'terser',
            terserOptions: {
              compress: {
                drop_console: true,
                drop_debugger: true
              }
            },
            
            // 资源处理
            assetsInlineLimit: 4096,
            chunkSizeWarningLimit: 500
          },
          
          // 优化依赖预构建
          optimizeDeps: {
            include: ['vue', 'vue-router', 'pinia'],
            exclude: ['your-local-package']
          }
        })
        """, language="javascript")

with build_col2:
    with st.expander("性能监控", expanded=True):
        st.code("""
        // plugins/performance.js
        export default {
          install: (app) => {
            // 性能标记
            const marks = new Map()

            // 性能监控方法
            const performance = {
              mark(name) {
                marks.set(name, performance.now())
              },
              
              measure(name, startMark, endMark) {
                const start = marks.get(startMark)
                const end = marks.get(endMark)
                if (start && end) {
                  console.log(`${name}: ${end - start}ms`)
                }
              },
              
              // 组件性能追踪
              trackComponent(component) {
                const { created, mounted } = component

                component.created = function() {
                  performance.mark(`${this.$options.name}-created-start`)
                  created?.call(this)
                  performance.mark(`${this.$options.name}-created-end`)
                  performance.measure(
                    `${this.$options.name} created`,
                    `${this.$options.name}-created-start`,
                    `${this.$options.name}-created-end`
                  )
                }

                component.mounted = function() {
                  performance.mark(`${this.$options.name}-mounted-start`)
                  mounted?.call(this)
                  performance.mark(`${this.$options.name}-mounted-end`)
                  performance.measure(
                    `${this.$options.name} mounted`,
                    `${this.$options.name}-mounted-start`,
                    `${this.$options.name}-mounted-end`
                  )
                }
              }
            }

            // 注册全局性能监控
            app.config.performance = true
            app.provide('performance', performance)
          }
        }

        // 使用示例
        <script setup>
        import { inject, onMounted } from 'vue'

        const performance = inject('performance')

        onMounted(() => {
          performance.mark('component-init')
          // 组件初始化逻辑
          performance.mark('component-ready')
          performance.measure(
            'Component Initialization',
            'component-init',
            'component-ready'
          )
        })
        </script>
        """, language="javascript")

