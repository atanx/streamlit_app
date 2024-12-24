import streamlit as st

st.title("Next.js 完整指南")

# 基础介绍
st.markdown("""
## 📚 使用指南

这个 Next.js 速查表涵盖了从入门到高级的所有主要概念，帮助你快速掌握 Next.js 开发。

### 🔍 内容索引
1. **基础概念**
   - 项目结构
   - 路由系统
   - 页面组件
   - 数据获取

2. **核心特性**
   - 服务端渲染 (SSR)
   - 静态生成 (SSG)
   - 增量静态再生成 (ISR)
   - API 路由

3. **数据获取**
   - getStaticProps
   - getServerSideProps
   - getStaticPaths
   - SWR 使用

4. **路由系统**
   - 文件系统路由
   - 动态路由
   - 嵌套路由
   - 中间件
""")

# 开始基础概念部分
st.header("基础概念")

concept_col1, concept_col2 = st.columns(2)

with concept_col1:
    with st.expander("项目结构", expanded=True):
        st.code("""
        my-nextjs-app/
        ├── pages/              # 页面目录
        │   ├── _app.js        # 应用入口
        │   ├── _document.js   # 自定义文档
        │   ├── index.js       # 首页
        │   └─���� api/           # API 路由
        ├── public/            # 静态资源
        ├── styles/            # 样式文件
        ├── components/        # 组件目录
        ├── lib/               # 工具函数
        ├── next.config.js     # Next.js 配置
        └── package.json       # 项目配置
        """, language="plaintext")
        
        st.markdown("""
        ### 关键目录说明
        - `pages/`: 所有页面组件
        - `public/`: 静态资源文件
        - `styles/`: CSS 样式文件
        - `components/`: 可复用组件
        - `lib/`: 工具函数和共享代码
        """)

with concept_col2:
    with st.expander("基础页面组件", expanded=True):
        st.code("""
        // pages/index.js
        import Head from 'next/head'
        
        export default function Home() {
          return (
            <div>
              <Head>
                <title>Next.js 示例</title>
                <meta name="description" content="Next.js 示例页面" />
              </Head>
              
              <main>
                <h1>欢迎使用 Next.js</h1>
                <p>这是一个基础页面组件</p>
              </main>
            </div>
          )
        }
        """, language="javascript")

# 添加路由示例
st.subheader("路由系统")

route_col1, route_col2 = st.columns(2)

with route_col1:
    with st.expander("基础路由", expanded=True):
        st.code("""
        // pages/about.js
        export default function About() {
          return <h1>关于我们</h1>
        }
        
        // pages/posts/[id].js
        import { useRouter } from 'next/router'
        
        export default function Post() {
          const router = useRouter()
          const { id } = router.query
          
          return <h1>文章 {id}</h1>
        }
        """, language="javascript")

with route_col2:
    with st.expander("路由导航", expanded=True):
        st.code("""
        import Link from 'next/link'
        import { useRouter } from 'next/router'
        
        export default function Navigation() {
          const router = useRouter()
          
          return (
            <nav>
              {/* 声明式导航 */}
              <Link href="/">
                首页
              </Link>
              
              <Link href="/about">
                关于
              </Link>
              
              {/* 编程式导航 */}
              <button onClick={() => router.push('/posts/1')}>
                查看文章
              </button>
              
              <button onClick={() => router.back()}>
                返回
              </button>
            </nav>
          )
        }
        """, language="javascript")

# 添加数据获取示例
st.subheader("数据获取方法")

data_col1, data_col2 = st.columns(2)

with data_col1:
    with st.expander("静态生成 (SSG)", expanded=True):
        st.code("""
        // pages/posts/[id].js
        export default function Post({ post }) {
          return (
            <article>
              <h1>{post.title}</h1>
              <div>{post.content}</div>
            </article>
          )
        }
        
        // 生成静态页面
        export async function getStaticProps({ params }) {
          const res = await fetch(
            `https://api.example.com/posts/${params.id}`
          )
          const post = await res.json()
          
          return {
            props: { post },
            // 每10秒重新生成
            revalidate: 10
          }
        }
        
        // 指定动态路由参数
        export async function getStaticPaths() {
          const res = await fetch('https://api.example.com/posts')
          const posts = await res.json()
          
          const paths = posts.map((post) => ({
            params: { id: post.id.toString() }
          }))
          
          return {
            paths,
            fallback: false
          }
        }
        """, language="javascript")

with data_col2:
    with st.expander("服务端渲染 (SSR)", expanded=True):
        st.code("""
        // pages/profile.js
        export default function Profile({ user }) {
          return (
            <div>
              <h1>个人资料</h1>
              <div>用户名: {user.name}</div>
              <div>邮箱: {user.email}</div>
            </div>
          )
        }
        
        // 服务端获取数据
        export async function getServerSideProps(context) {
          const { req, res } = context
          const { cookies } = req
          
          // 获取用户信息
          const response = await fetch(
            'https://api.example.com/user',
            {
              headers: {
                Cookie: cookies.token
              }
            }
          )
          
          const user = await response.json()
          
          if (!user) {
            return {
              redirect: {
                destination: '/login',
                permanent: false
              }
            }
          }
          
          return {
            props: { user }
          }
        }
        """, language="javascript")

# 添加高级路由特性
st.header("高级路由特性")

advanced_route_col1, advanced_route_col2 = st.columns(2)

with advanced_route_col1:
    with st.expander("中间件 (Middleware)", expanded=True):
        st.code("""
        // middleware.ts
        import { NextResponse } from 'next/server'
        import type { NextRequest } from 'next/server'

        export function middleware(request: NextRequest) {
          // 获取token
          const token = request.cookies.get('token')
          
          // 保护路由
          if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
            return NextResponse.redirect(new URL('/login', request.url))
          }
          
          // 添加自定义头部
          const response = NextResponse.next()
          response.headers.set('x-custom-header', 'my-value')
          
          // 国际化重定向
          if (request.nextUrl.pathname === '/') {
            const language = request.cookies.get('NEXT_LOCALE') || 'en'
            return NextResponse.redirect(new URL(`/${language}`, request.url))
          }
          
          return response
        }

        export const config = {
          matcher: [
            '/dashboard/:path*',
            '/((?!api|_next/static|favicon.ico).*)'
          ]
        }
        """, language="typescript")

with advanced_route_col2:
    with st.expander("动态路由模式", expanded=True):
        st.code("""
        // pages/posts/[[...slug]].js
        import { useRouter } from 'next/router'

        export default function Post() {
          const router = useRouter()
          const { slug } = router.query
          
          // 可选捕获所有路由
          // /posts
          // /posts/a
          // /posts/a/b
          // /posts/a/b/c
          
          return (
            <div>
              <h1>文章路径: {slug ? slug.join('/') : '首页'}</h1>
            </div>
          )
        }

        // pages/products/[...categories].js
        export default function Category() {
          const router = useRouter()
          const { categories } = router.query
          
          // 捕获所有路由
          // /products/clothes
          // /products/clothes/shirts
          // /products/clothes/shirts/summer
          
          return (
            <div>
              <h1>分类: {categories?.join(' > ')}</h1>
            </div>
          )
        }
        """, language="javascript")

# 添加样式解决方案
st.header("样式解决方案")

style_col1, style_col2 = st.columns(2)

with style_col1:
    with st.expander("CSS Modules", expanded=True):
        st.code("""
        // styles/Button.module.css
        .button {
          padding: 1rem 2rem;
          border-radius: 4px;
          font-weight: bold;
        }

        .primary {
          background: blue;
          color: white;
        }

        .secondary {
          background: gray;
          color: black;
        }

        // components/Button.js
        import styles from '../styles/Button.module.css'

        export default function Button({ variant = 'primary', children }) {
          return (
            <button className={`${styles.button} ${styles[variant]}`}>
              {children}
            </button>
          )
        }
        """, language="javascript")

with style_col2:
    with st.expander("Tailwind CSS", expanded=True):
        st.code("""
        // tailwind.config.js
        module.exports = {
          content: [
            './pages/**/*.{js,ts,jsx,tsx}',
            './components/**/*.{js,ts,jsx,tsx}',
          ],
          theme: {
            extend: {
              colors: {
                primary: '#1a73e8',
                secondary: '#5f6368',
              },
            },
          },
          plugins: [],
        }

        // components/Card.js
        export default function Card({ title, description }) {
          return (
            <div className="p-6 max-w-sm mx-auto bg-white rounded-xl 
                          shadow-md flex items-center space-x-4">
              <div>
                <h3 className="text-xl font-medium text-primary">
                  {title}
                </h3>
                <p className="text-secondary">
                  {description}
                </p>
              </div>
            </div>
          )
        }
        """, language="javascript")

# 添加样式最佳实践
st.subheader("样式最佳实践")

style_best_col1, style_best_col2 = st.columns(2)

with style_best_col1:
    with st.expander("CSS-in-JS (Styled Components)", expanded=True):
        st.code("""
        // components/StyledButton.js
        import styled from 'styled-components'

        const Button = styled.button`
          padding: 1rem 2rem;
          border-radius: 4px;
          font-weight: bold;
          background: ${props => props.primary ? 'blue' : 'gray'};
          color: ${props => props.primary ? 'white' : 'black'};
          
          &:hover {
            opacity: 0.8;
          }
          
          @media (max-width: 768px) {
            padding: 0.5rem 1rem;
          }
        `

        export default function StyledButton({ primary, children }) {
          return (
            <Button primary={primary}>
              {children}
            </Button>
          )
        }
        """, language="javascript")

with style_best_col2:
    with st.expander("全局样式", expanded=True):
        st.code("""
        // pages/_app.js
        import '../styles/globals.css'
        import { ThemeProvider } from 'styled-components'

        const theme = {
          colors: {
            primary: '#1a73e8',
            secondary: '#5f6368',
            background: '#ffffff',
            text: '#202124',
          },
          breakpoints: {
            mobile: '320px',
            tablet: '768px',
            desktop: '1024px',
          },
        }

        export default function MyApp({ Component, pageProps }) {
          return (
            <ThemeProvider theme={theme}>
              <Component {...pageProps} />
            </ThemeProvider>
          )
        }

        // styles/globals.css
        @tailwind base;
        @tailwind components;
        @tailwind utilities;

        :root {
          --primary-color: #1a73e8;
          --secondary-color: #5f6368;
        }

        * {
          box-sizing: border-box;
          margin: 0;
          padding: 0;
        }

        body {
          font-family: -apple-system, system-ui, sans-serif;
          line-height: 1.5;
        }
        """, language="javascript")

# 添加 API 路由
st.header("API 路由")

api_col1, api_col2 = st.columns(2)

with api_col1:
    with st.expander("基础 API 路由", expanded=True):
        st.code("""
        // pages/api/hello.js
        export default function handler(req, res) {
          if (req.method === 'GET') {
            res.status(200).json({ message: 'Hello World!' })
          } else {
            res.status(405).json({ message: '方法不允许' })
          }
        }

        // pages/api/posts/[id].js
        export default function handler(req, res) {
          const { id } = req.query
          
          switch (req.method) {
            case 'GET':
              // 获取文章
              res.status(200).json({ id, title: '文章标题' })
              break
              
            case 'PUT':
              // 更新文章
              const { title, content } = req.body
              res.status(200).json({ id, title, content })
              break
              
            case 'DELETE':
              // 删除文章
              res.status(200).json({ message: '删除成功' })
              break
              
            default:
              res.status(405).json({ message: '方法不允许' })
          }
        }
        """, language="javascript")

with api_col2:
    with st.expander("API 中间件", expanded=True):
        st.code("""
        // middleware/auth.js
        export function withAuth(handler) {
          return async (req, res) => {
            // 获取认证token
            const token = req.headers.authorization?.split(' ')[1]
            
            if (!token) {
              return res.status(401).json({ 
                message: '未认证' 
              })
            }
            
            try {
              // 验证token
              const decoded = jwt.verify(token, process.env.JWT_SECRET)
              req.user = decoded
              
              // 继续处理请求
              return handler(req, res)
            } catch (error) {
              return res.status(401).json({ 
                message: '认证失败' 
              })
            }
          }
        }

        // pages/api/protected.js
        import { withAuth } from '../../middleware/auth'

        function handler(req, res) {
          // 已认证的路由
          res.status(200).json({ 
            message: '受保护的数据',
            user: req.user 
          })
        }

        export default withAuth(handler)
        """, language="javascript")

# 添加性能优化
st.header("性能优化")

perf_col1, perf_col2 = st.columns(2)

with perf_col1:
    with st.expander("图片优化", expanded=True):
        st.code("""
        // next.config.js
        module.exports = {
          images: {
            domains: ['example.com'],
            formats: ['image/avif', 'image/webp'],
            deviceSizes: [640, 750, 828, 1080, 1200],
            imageSizes: [16, 32, 48, 64, 96],
          },
        }

        // components/OptimizedImage.js
        import Image from 'next/image'

        export default function OptimizedImage() {
          return (
            <div>
              <Image
                src="/hero.jpg"
                alt="Hero image"
                width={1200}
                height={600}
                priority
                placeholder="blur"
                blurDataURL="data:image/jpeg;base64,..."
              />
              
              <Image
                src="https://example.com/photo.jpg"
                alt="Remote image"
                width={800}
                height={400}
                loading="lazy"
              />
            </div>
          )
        }
        """, language="javascript")

with perf_col2:
    with st.expander("动态导入", expanded=True):
        st.code("""
        // components/HeavyComponent.js
        import dynamic from 'next/dynamic'

        // 动态导入组件
        const DynamicChart = dynamic(
          () => import('../components/Chart'),
          {
            loading: () => <p>加载中...</p>,
            ssr: false // 禁用服务端渲染
          }
        )

        // 动态导入库
        const DynamicMap = dynamic(
          () => import('../components/Map').then(mod => mod.Map),
          {
            loading: () => <p>地图加载中...</p>,
            ssr: false
          }
        )

        export default function Dashboard() {
          return (
            <div>
              <DynamicChart />
              <DynamicMap />
            </div>
          )
        }
        """, language="javascript")

# 添加缓存策略
st.subheader("缓存优化")

cache_col1, cache_col2 = st.columns(2)

with cache_col1:
    with st.expander("SWR 数据缓存", expanded=True):
        st.code("""
        // hooks/useData.js
        import useSWR from 'swr'

        const fetcher = url => fetch(url).then(r => r.json())

        export function useUser(id) {
          const { data, error, mutate } = useSWR(
            `/api/users/${id}`,
            fetcher,
            {
              revalidateOnFocus: false,
              revalidateOnReconnect: false,
              refreshInterval: 30000 // 30秒刷新一次
            }
          )

          return {
            user: data,
            isLoading: !error && !data,
            isError: error,
            mutate // 手动重新验证
          }
        }

        // 使用示例
        function Profile({ id }) {
          const { user, isLoading } = useUser(id)

          if (isLoading) return <div>加载中...</div>
          
          return (
            <div>
              <h1>{user.name}</h1>
              <p>{user.email}</p>
            </div>
          )
        }
        """, language="javascript")

with cache_col2:
    with st.expander("静态页面缓存", expanded=True):
        st.code("""
        // pages/posts/[id].js
        export default function Post({ post }) {
          return (
            <article>
              <h1>{post.title}</h1>
              <div>{post.content}</div>
            </article>
          )
        }

        export async function getStaticProps({ params }) {
          const post = await fetchPost(params.id)
          
          return {
            props: {
              post,
            },
            // 增量静态再生成
            revalidate: 60, // 60秒后重新生成
          }
        }

        // 自定义缓存控制
        export function generateHeaders() {
          return {
            'Cache-Control': 'public, s-maxage=10, stale-while-revalidate=59'
          }
        }

        // 页面组件中使用
        export async function getServerSideProps({ res }) {
          res.setHeader(
            'Cache-Control',
            'public, s-maxage=10, stale-while-revalidate=59'
          )
          
          return {
            props: {
              // ...
            }
          }
        }
        """, language="javascript")

# 添加部署策略
st.header("部署策略")

deploy_col1, deploy_col2 = st.columns(2)

with deploy_col1:
    with st.expander("生产环境配置", expanded=True):
        st.code("""
        // next.config.js
        module.exports = {
          // 生产环境配置
          productionBrowserSourceMaps: false,
          compress: true,
          poweredByHeader: false,
          
          // 环境变量
          env: {
            API_URL: process.env.API_URL,
            GA_TRACKING_ID: process.env.GA_TRACKING_ID,
          },
          
          // CDN 配置
          assetPrefix: process.env.CDN_URL,
          
          // 输出配置
          output: 'standalone',
          
          // 优化配置
          experimental: {
            optimizeCss: true,
            scrollRestoration: true,
          },
        }

        // package.json
        {
          "scripts": {
            "build": "next build",
            "start": "next start -p $PORT",
            "analyze": "ANALYZE=true next build"
          }
        }
        """, language="javascript")

with deploy_col2:
    with st.expander("Docker部署", expanded=True):
        st.code("""
        # Dockerfile
        FROM node:18-alpine AS base

        # 依赖阶段
        FROM base AS deps
        WORKDIR /app
        COPY package.json package-lock.json ./
        RUN npm ci

        # 构建阶段
        FROM base AS builder
        WORKDIR /app
        COPY --from=deps /app/node_modules ./node_modules
        COPY . .
        RUN npm run build

        # 生产阶段
        FROM base AS runner
        WORKDIR /app
        ENV NODE_ENV production

        # 复制必要文件
        COPY --from=builder /app/public ./public
        COPY --from=builder /app/.next/standalone ./
        COPY --from=builder /app/.next/static ./.next/static

        EXPOSE 3000
        ENV PORT 3000
        CMD ["node", "server.js"]

        # docker-compose.yml
        version: '3'
        services:
          web:
            build: .
            ports:
              - "3000:3000"
            environment:
              - DATABASE_URL=postgres://user:pass@db:5432/dbname
              - REDIS_URL=redis://cache:6379
            depends_on:
              - db
              - cache
          
          db:
            image: postgres:14
            environment:
              POSTGRES_USER: user
              POSTGRES_PASSWORD: pass
              POSTGRES_DB: dbname
          
          cache:
            image: redis:6
        """, language="dockerfile")

# 添加测试方案
st.header("测试方案")

test_col1, test_col2 = st.columns(2)

with test_col1:
    with st.expander("单元测试", expanded=True):
        st.code("""
        // __tests__/components/Button.test.js
        import { render, fireEvent } from '@testing-library/react'
        import Button from '@/components/Button'

        describe('Button Component', () => {
          it('renders correctly', () => {
            const { getByText } = render(
              <Button>Click me</Button>
            )
            
            expect(getByText('Click me')).toBeInTheDocument()
          })

          it('handles click events', () => {
            const handleClick = jest.fn()
            const { getByText } = render(
              <Button onClick={handleClick}>Click me</Button>
            )
            
            fireEvent.click(getByText('Click me'))
            expect(handleClick).toHaveBeenCalledTimes(1)
          })

          it('applies custom styles', () => {
            const { container } = render(
              <Button variant="primary">Styled Button</Button>
            )
            
            expect(container.firstChild).toHaveClass('primary')
          })
        })

        // jest.config.js
        module.exports = {
          testEnvironment: 'jsdom',
          setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
          testPathIgnorePatterns: [
            '<rootDir>/.next/',
            '<rootDir>/node_modules/'
          ],
          moduleNameMapper: {
            '^@/components/(.*)$': '<rootDir>/components/$1',
            '\\.(css|less|scss|sass)$': 'identity-obj-proxy'
          }
        }
        """, language="javascript")

with test_col2:
    with st.expander("集成测试", expanded=True):
        st.code("""
        // cypress/integration/home.spec.js
        describe('Home Page', () => {
          beforeEach(() => {
            cy.visit('/')
          })

          it('displays the header', () => {
            cy.get('h1')
              .should('be.visible')
              .and('contain', 'Welcome')
          })

          it('navigates to about page', () => {
            cy.get('nav')
              .contains('About')
              .click()
            
            cy.url()
              .should('include', '/about')
          })

          it('handles form submission', () => {
            cy.intercept('POST', '/api/contact', {
              statusCode: 200,
              body: { message: 'Success' }
            }).as('submitForm')

            cy.get('input[name="email"]')
              .type('test@example.com')
            
            cy.get('textarea[name="message"]')
              .type('Hello, World!')
            
            cy.get('form')
              .submit()

            cy.wait('@submitForm')
            cy.get('.success-message')
              .should('be.visible')
          })
        })

        // cypress.config.js
        const { defineConfig } = require('cypress')

        module.exports = defineConfig({
          e2e: {
            baseUrl: 'http://localhost:3000',
            supportFile: false,
            video: false,
            screenshotOnRunFailure: false,
          },
        })
        """, language="javascript")

# 添加测试最佳实践
st.subheader("测试最佳实践")

test_best_col1, test_best_col2 = st.columns(2)

with test_best_col1:
    with st.expander("API测试", expanded=True):
        st.code("""
        // __tests__/api/users.test.js
        import { createMocks } from 'node-mocks-http'
        import handler from '@/pages/api/users'

        describe('Users API', () => {
          it('creates a user', async () => {
            const { req, res } = createMocks({
              method: 'POST',
              body: {
                name: 'John Doe',
                email: 'john@example.com'
              }
            })

            await handler(req, res)

            expect(res._getStatusCode()).toBe(201)
            expect(JSON.parse(res._getData())).toEqual(
              expect.objectContaining({
                id: expect.any(String),
                name: 'John Doe',
                email: 'john@example.com'
              })
            )
          })

          it('handles validation errors', async () => {
            const { req, res } = createMocks({
              method: 'POST',
              body: {
                name: 'John Doe'
                // missing email
              }
            })

            await handler(req, res)

            expect(res._getStatusCode()).toBe(400)
            expect(JSON.parse(res._getData())).toEqual({
              error: 'Email is required'
            })
          })
        })
        """, language="javascript")

with test_best_col2:
    with st.expander("自定义渲染", expanded=True):
        st.code("""
        // test/utils.js
        import { render } from '@testing-library/react'
        import { ThemeProvider } from 'styled-components'
        import { SWRConfig } from 'swr'

        const theme = {
          colors: {
            primary: '#000',
            secondary: '#666'
          }
        }

        export function renderWithProviders(
          ui,
          { theme = theme, ...options } = {}
        ) {
          return render(
            <ThemeProvider theme={theme}>
              <SWRConfig value={{ 
                provider: () => new Map(),
                dedupingInterval: 0 
              }}>
                {ui}
              </SWRConfig>
            </ThemeProvider>,
            options
          )
        }

        // 使用示例
        import { renderWithProviders } from '../test/utils'

        test('renders with theme', () => {
          const { getByText } = renderWithProviders(
            <Button>Themed Button</Button>
          )
          
          expect(getByText('Themed Button'))
            .toHaveStyle('color: #000')
        })
        """, language="javascript")

# 添加状态管理
st.header("状态管理")

state_col1, state_col2 = st.columns(2)

with state_col1:
    with st.expander("Context API", expanded=True):
        st.code("""
        // context/AppContext.js
        import { createContext, useContext, useReducer } from 'react'

        const AppContext = createContext()

        const initialState = {
          user: null,
          theme: 'light',
          language: 'en'
        }

        function reducer(state, action) {
          switch (action.type) {
            case 'SET_USER':
              return { ...state, user: action.payload }
            case 'SET_THEME':
              return { ...state, theme: action.payload }
            case 'SET_LANGUAGE':
              return { ...state, language: action.payload }
            default:
              return state
          }
        }

        export function AppProvider({ children }) {
          const [state, dispatch] = useReducer(reducer, initialState)

          return (
            <AppContext.Provider value={{ state, dispatch }}>
              {children}
            </AppContext.Provider>
          )
        }

        export function useApp() {
          const context = useContext(AppContext)
          if (!context) {
            throw new Error('useApp must be used within AppProvider')
          }
          return context
        }

        // pages/_app.js
        import { AppProvider } from '../context/AppContext'

        export default function MyApp({ Component, pageProps }) {
          return (
            <AppProvider>
              <Component {...pageProps} />
            </AppProvider>
          )
        }
        """, language="javascript")

with state_col2:
    with st.expander("Zustand状态管理", expanded=True):
        st.code("""
        // store/useStore.js
        import create from 'zustand'
        import { persist } from 'zustand/middleware'

        const useStore = create(
          persist(
            (set, get) => ({
              // 状态
              cart: [],
              user: null,
              theme: 'light',
              
              // 操作
              addToCart: (product) => set((state) => ({
                cart: [...state.cart, product]
              })),
              
              removeFromCart: (productId) => set((state) => ({
                cart: state.cart.filter(item => item.id !== productId)
              })),
              
              setUser: (user) => set({ user }),
              
              toggleTheme: () => set((state) => ({
                theme: state.theme === 'light' ? 'dark' : 'light'
              })),
              
              // 计算属性
              get cartTotal() {
                return get().cart.reduce(
                  (total, item) => total + item.price,
                  0
                )
              }
            }),
            {
              name: 'app-storage',
              getStorage: () => localStorage
            }
          )
        )

        export default useStore

        // 使用示例
        function Cart() {
          const { cart, removeFromCart, cartTotal } = useStore()
          
          return (
            <div>
              {cart.map(item => (
                <div key={item.id}>
                  <span>{item.name}</span>
                  <button onClick={() => removeFromCart(item.id)}>
                    删除
                  </button>
                </div>
              ))}
              <div>总计: ${cartTotal}</div>
            </div>
          )
        }
        """, language="javascript")

# 添加国际化
st.header("国际化 (i18n)")

i18n_col1, i18n_col2 = st.columns(2)

with i18n_col1:
    with st.expander("基础配置", expanded=True):
        st.code("""
        // next.config.js
        module.exports = {
          i18n: {
            locales: ['en', 'zh', 'ja'],
            defaultLocale: 'en',
            localeDetection: true,
            domains: [
              {
                domain: 'example.com',
                defaultLocale: 'en'
              },
              {
                domain: 'example.cn',
                defaultLocale: 'zh'
              },
              {
                domain: 'example.jp',
                defaultLocale: 'ja'
              }
            ]
          }
        }

        // next-i18next.config.js
        module.exports = {
          i18n: {
            defaultLocale: 'en',
            locales: ['en', 'zh', 'ja'],
          },
          localePath: './public/locales',
          reloadOnPrerender: process.env.NODE_ENV === 'development'
        }
        """, language="javascript")

with i18n_col2:
    with st.expander("翻译实现", expanded=True):
        st.code("""
        // public/locales/en/common.json
        {
          "welcome": "Welcome",
          "about": {
            "title": "About Us",
            "description": "We are a team..."
          },
          "error": {
            "required": "This field is required",
            "invalid_email": "Invalid email address"
          }
        }

        // pages/index.js
        import { useTranslation } from 'next-i18next'
        import { serverSideTranslations } from 'next-i18next/serverSideTranslations'

        export default function Home() {
          const { t } = useTranslation('common')

          return (
            <div>
              <h1>{t('welcome')}</h1>
              <div>
                <h2>{t('about.title')}</h2>
                <p>{t('about.description')}</p>
              </div>
            </div>
          )
        }

        export async function getStaticProps({ locale }) {
          return {
            props: {
              ...(await serverSideTranslations(locale, ['common']))
            }
          }
        }

        // components/LanguageSwitcher.js
        import { useRouter } from 'next/router'

        export default function LanguageSwitcher() {
          const router = useRouter()
          const { locales, locale: activeLocale } = router

          const handleLocaleChange = (locale) => {
            router.push(router.pathname, router.asPath, { locale })
          }

          return (
            <div>
              {locales.map((locale) => (
                <button
                  key={locale}
                  onClick={() => handleLocaleChange(locale)}
                  disabled={locale === activeLocale}
                >
                  {locale.toUpperCase()}
                </button>
              ))}
            </div>
          )
        }
        """, language="javascript")

# 添加 SEO 优化
st.header("SEO 优化")

seo_col1, seo_col2 = st.columns(2)

with seo_col1:
    with st.expander("基础 SEO", expanded=True):
        st.code("""
        // components/SEO.js
        import Head from 'next/head'

        export default function SEO({
          title,
          description,
          canonical,
          openGraph,
          twitter
        }) {
          return (
            <Head>
              <title>{title}</title>
              <meta name="description" content={description} />
              <link rel="canonical" href={canonical} />
              
              {/* Open Graph */}
              <meta property="og:title" content={openGraph?.title || title} />
              <meta 
                property="og:description" 
                content={openGraph?.description || description} 
              />
              <meta property="og:type" content={openGraph?.type || 'website'} />
              <meta property="og:image" content={openGraph?.image} />
              
              {/* Twitter Card */}
              <meta name="twitter:card" content="summary_large_image" />
              <meta name="twitter:title" content={twitter?.title || title} />
              <meta 
                name="twitter:description" 
                content={twitter?.description || description} 
              />
              <meta name="twitter:image" content={twitter?.image} />
              
              {/* 结构化数据 */}
              <script
                type="application/ld+json"
                dangerouslySetInnerHTML={{
                  __html: JSON.stringify({
                    '@context': 'https://schema.org',
                    '@type': 'WebPage',
                    name: title,
                    description: description,
                    url: canonical
                  })
                }}
              />
            </Head>
          )
        }

        // pages/blog/[slug].js
        export default function BlogPost({ post }) {
          return (
            <>
              <SEO
                title={post.title}
                description={post.excerpt}
                canonical={`https://example.com/blog/${post.slug}`}
                openGraph={{
                  type: 'article',
                  image: post.coverImage
                }}
              />
              <article>{/* 文章内容 */}</article>
            </>
          )
        }
        """, language="javascript")

with seo_col2:
    with st.expander("动态站点地图", expanded=True):
        st.code("""
        // pages/sitemap.xml.js
        function generateSiteMap(posts) {
          return `<?xml version="1.0" encoding="UTF-8"?>
            <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
              <!-- 添加静态页面 -->
              <url>
                <loc>https://example.com</loc>
                <lastmod>${new Date().toISOString()}</lastmod>
                <changefreq>daily</changefreq>
                <priority>1.0</priority>
              </url>
              
              <!-- 添加动态页面 -->
              ${posts.map(post => `
                <url>
                  <loc>https://example.com/blog/${post.slug}</loc>
                  <lastmod>${post.updatedAt}</lastmod>
                  <changefreq>weekly</changefreq>
                  <priority>0.8</priority>
                </url>
              `).join('')}
            </urlset>
          `
        }

        export async function getServerSideProps({ res }) {
          // 获取所有文章
          const posts = await getAllPosts()
          
          // 生成站点地图
          const sitemap = generateSiteMap(posts)
          
          res.setHeader('Content-Type', 'text/xml')
          res.write(sitemap)
          res.end()
          
          return {
            props: {}
          }
        }

        export default function Sitemap() {
          // 页面组件为空，因为我们只需要生成 XML
          return null
        }
        """, language="javascript")

# 添加错误处理
st.header("错误处理")

error_col1, error_col2 = st.columns(2)

with error_col1:
    with st.expander("全局���误处理", expanded=True):
        st.code("""
        // pages/_error.js
        function Error({ statusCode }) {
          return (
            <div>
              {statusCode
                ? `服务器返回错误 ${statusCode}`
                : '客户端发生错误'}
            </div>
          )
        }

        Error.getInitialProps = ({ res, err }) => {
          const statusCode = res ? res.statusCode : err ? err.statusCode : 404
          return { statusCode }
        }

        export default Error

        // pages/404.js
        export default function Custom404() {
          return <h1>404 - 页面未找到</h1>
        }

        // pages/500.js
        export default function Custom500() {
          return <h1>500 - 服务器错误</h1>
        }

        // pages/_app.js
        export default function MyApp({ Component, pageProps }) {
          return (
            <ErrorBoundary>
              <Component {...pageProps} />
            </ErrorBoundary>
          )
        }

        class ErrorBoundary extends React.Component {
          constructor(props) {
            super(props)
            this.state = { hasError: false }
          }

          static getDerivedStateFromError(error) {
            return { hasError: true }
          }

          componentDidCatch(error, errorInfo) {
            // 记录错误到日志服务
            logErrorToService(error, errorInfo)
          }

          render() {
            if (this.state.hasError) {
              return <h1>出错了！</h1>
            }

            return this.props.children
          }
        }
        """, language="javascript")

with error_col2:
    with st.expander("API 错误处理", expanded=True):
        st.code("""
        // lib/errors.js
        export class APIError extends Error {
          constructor(statusCode, message) {
            super(message)
            this.statusCode = statusCode
          }
        }

        export function withErrorHandler(handler) {
          return async (req, res) => {
            try {
              await handler(req, res)
            } catch (error) {
              if (error instanceof APIError) {
                res.status(error.statusCode).json({
                  error: error.message
                })
              } else {
                console.error(error)
                res.status(500).json({
                  error: '服务器内部错误'
                })
              }
            }
          }
        }

        // pages/api/users/[id].js
        import { APIError, withErrorHandler } from '../../../lib/errors'

        async function handler(req, res) {
          const { id } = req.query

          if (!id) {
            throw new APIError(400, '缺少用户ID')
          }

          try {
            const user = await db.user.findUnique({
              where: { id }
            })

            if (!user) {
              throw new APIError(404, '用户未找到')
            }

            res.json(user)
          } catch (error) {
            throw new APIError(500, '数据库错误')
          }
        }

        export default withErrorHandler(handler)
        """, language="javascript")

# 添加监控和日志
st.header("监控和日志")

monitor_col1, monitor_col2 = st.columns(2)

with monitor_col1:
    with st.expander("性能监控", expanded=True):
        st.code("""
        // lib/analytics.js
        export function reportWebVitals(metric) {
          const { id, name, label, value } = metric
          
          // 发送到分析服务
          analytics.send({
            metric_name: name,
            metric_value: value,
            metric_id: id,
            metric_label: label
          })
          
          // 自定义指标监控
          if (name === 'FCP') {
            console.log('First Contentful Paint:', value)
          }
          if (name === 'LCP') {
            console.log('Largest Contentful Paint:', value)
          }
          if (name === 'CLS') {
            console.log('Cumulative Layout Shift:', value)
          }
          if (name === 'FID') {
            console.log('First Input Delay:', value)
          }
          if (name === 'TTFB') {
            console.log('Time to First Byte:', value)
          }
        }

        // pages/_app.js
        export function reportWebVitals(metric) {
          switch (metric.name) {
            case 'FCP':
              // 处理首次内容绘制
              break
            case 'LCP':
              // 处理最大内容绘制
              break
            case 'CLS':
              // 处理累积布局偏移
              break
            case 'FID':
              // 处理首次输入延迟
              break
            case 'TTFB':
              // 处理首字节时间
              break
            default:
              break
          }
        }
        """, language="javascript")

with monitor_col2:
    with st.expander("错误日志", expanded=True):
        st.code("""
        // lib/logger.js
        import pino from 'pino'

        const logger = pino({
          level: process.env.LOG_LEVEL || 'info',
          transport: {
            target: 'pino-pretty',
            options: {
              colorize: true
            }
          }
        })

        class Logger {
          static info(message, data = {}) {
            logger.info({ ...data }, message)
          }

          static error(error, context = {}) {
            logger.error({
              error: {
                message: error.message,
                stack: error.stack
              },
              ...context
            })
          }

          static warn(message, data = {}) {
            logger.warn({ ...data }, message)
          }

          static debug(message, data = {}) {
            logger.debug({ ...data }, message)
          }
        }

        // 使用示例
        try {
          throw new Error('发生错误')
        } catch (error) {
          Logger.error(error, {
            context: 'API调用',
            userId: 'user123'
          })
        }

        // 中间件使用
        export function loggerMiddleware(req, res, next) {
          const start = Date.now()
          
          res.on('finish', () => {
            const duration = Date.now() - start
            Logger.info('API请求', {
              method: req.method,
              url: req.url,
              status: res.statusCode,
              duration
            })
          })
          
          next()
        }
        """, language="javascript")

# 添加安全配置
st.header("安全配置")

security_col1, security_col2 = st.columns(2)

with security_col1:
    with st.expander("安全头部", expanded=True):
        st.code("""
        // next.config.js
        const securityHeaders = [
          {
            key: 'X-DNS-Prefetch-Control',
            value: 'on'
          },
          {
            key: 'Strict-Transport-Security',
            value: 'max-age=63072000; includeSubDomains; preload'
          },
          {
            key: 'X-XSS-Protection',
            value: '1; mode=block'
          },
          {
            key: 'X-Frame-Options',
            value: 'SAMEORIGIN'
          },
          {
            key: 'X-Content-Type-Options',
            value: 'nosniff'
          },
          {
            key: 'Referrer-Policy',
            value: 'origin-when-cross-origin'
          },
          {
            key: 'Content-Security-Policy',
            value: ContentSecurityPolicy.replace(/\\s{2,}/g, ' ').trim()
          }
        ]

        module.exports = {
          async headers() {
            return [
              {
                source: '/:path*',
                headers: securityHeaders,
              },
            ]
          },
        }

        // 内容安全策略
        const ContentSecurityPolicy = `
          default-src 'self';
          script-src 'self' 'unsafe-eval' 'unsafe-inline';
          style-src 'self' 'unsafe-inline';
          img-src 'self' data: https:;
          font-src 'self';
          object-src 'none';
          base-uri 'self';
          form-action 'self';
          frame-ancestors 'none';
          block-all-mixed-content;
          upgrade-insecure-requests;
        `
        """, language="javascript")

with security_col2:
    with st.expander("认证和授权", expanded=True):
        st.code("""
        // lib/auth.js
        import { getSession } from 'next-auth/react'
        import { verify } from 'jsonwebtoken'

        export function withAuth(handler) {
          return async (req, res) => {
            try {
              const session = await getSession({ req })
              
              if (!session) {
                return res.status(401).json({ 
                  error: '未认证' 
                })
              }
              
              // 添加用户信息到请求
              req.user = session.user
              return handler(req, res)
            } catch (error) {
              return res.status(401).json({ 
                error: '认证失败' 
              })
            }
          }
        }

        export function withRoles(roles) {
          return (handler) => {
            return async (req, res) => {
              try {
                const session = await getSession({ req })
                
                if (!session) {
                  return res.status(401).json({ 
                    error: '未认证' 
                  })
                }
                
                const hasRole = roles.some(
                  role => session.user.roles.includes(role)
                )
                
                if (!hasRole) {
                  return res.status(403).json({ 
                    error: '权限不足' 
                  })
                }
                
                return handler(req, res)
              } catch (error) {
                return res.status(401).json({ 
                  error: '认证失败' 
                })
              }
            }
          }
        }

        // 使用示例
        // pages/api/admin/users.js
        import { withAuth, withRoles } from '../../../lib/auth'

        async function handler(req, res) {
          // 处理管理员API
          res.json({ users: [] })
        }

        export default withAuth(
          withRoles(['admin'])(handler)
        )
        """, language="javascript")



# 添加缓存策略
st.header("缓存策略")

cache_col1, cache_col2 = st.columns(2)

with cache_col1:
    with st.expander("HTTP 缓存", expanded=True):
        st.code("""
        // pages/api/[...slug].js
        export default function handler(req, res) {
          // 设置缓存控制头
          res.setHeader('Cache-Control', `
            public, 
            s-maxage=10, 
            stale-while-revalidate=59
          `)
          
          // 设置 ETag
          const etag = generateETag(data)
          res.setHeader('ETag', etag)
          
          // 检查 If-None-Match
          const ifNoneMatch = req.headers['if-none-match']
          if (ifNoneMatch === etag) {
            res.status(304).end()
            return
          }
          
          res.json(data)
        }

        // middleware/cache.js
        export function withCache(handler) {
          return async (req, res) => {
            // 检查是否应该缓存
            if (!isCacheable(req)) {
              return handler(req, res)
            }
            
            const key = generateCacheKey(req)
            const cached = await getFromCache(key)
            
            if (cached) {
              res.setHeader('X-Cache', 'HIT')
              return res.json(cached)
            }
            
            // 修改响应对象以捕获数据
            const originalJson = res.json
            res.json = async (data) => {
              await setToCache(key, data)
              return originalJson.call(res, data)
            }
            
            return handler(req, res)
          }
        }
        """, language="javascript")

with cache_col2:
    with st.expander("状态缓存", expanded=True):
        st.code("""
        // lib/cache.js
        import Redis from 'ioredis'
import { serialize, deserialize } from 'superjson'

class Cache {
  constructor() {
    this.redis = new Redis(process.env.REDIS_URL)
    this.memoryCache = new Map()
  }
  
  async get(key) {
    // 先检查内存缓存
    if (this.memoryCache.has(key)) {
      const { value, expiry } = this.memoryCache.get(key)
      if (expiry > Date.now()) {
        return value
      }
      this.memoryCache.delete(key)
    }
    
    // 检查 Redis 缓存
    const data = await this.redis.get(key)
    if (data) {
      const value = deserialize(data)
      this.memoryCache.set(key, {
        value,
        expiry: Date.now() + 60000 // 1分钟
      })
      return value
    }
    
    return null
  }
  
  async set(key, value, ttl = 3600) {
    const serialized = serialize(value)
    await this.redis.setex(key, ttl, serialized)
    
    this.memoryCache.set(key, {
      value,
      expiry: Date.now() + 60000
    })
  }
  
  async invalidate(pattern) {
    const keys = await this.redis.keys(pattern)
    if (keys.length) {
      await this.redis.del(keys)
    }
    
    // 清除匹配的内存缓存
    for (const [key] of this.memoryCache) {
      if (key.match(pattern)) {
        this.memoryCache.delete(key)
      }
    }
  }
}

export const cache = new Cache()

// 使用示例
async function getUserProfile(userId) {
  const cacheKey = `user:${userId}:profile`
  
  // 尝试从缓存获取
  const cached = await cache.get(cacheKey)
  if (cached) {
    return cached
  }
  
  // 获取新数据
  const profile = await fetchUserProfile(userId)
  
  // 存入缓存
  await cache.set(cacheKey, profile)
  
  return profile
}
        """, language="javascript")

# 添加微前端集成
st.header("微前端集成")

micro_col1, micro_col2 = st.columns(2)

with micro_col1:
    with st.expander("Module Federation", expanded=True):
        st.code("""
        // next.config.js
        const { withModuleFederation } = require('@module-federation/nextjs-mf')

        module.exports = withModuleFederation({
          name: 'host',
          remotes: {
            shop: 'shop@http://localhost:3001/_next/static/chunks/remoteEntry.js',
            blog: 'blog@http://localhost:3002/_next/static/chunks/remoteEntry.js'
          },
          shared: {
            react: {
              singleton: true,
              requiredVersion: false
            },
            'react-dom': {
              singleton: true,
              requiredVersion: false
            }
          }
        })

        // pages/index.js
        import dynamic from 'next/dynamic'

        const RemoteShop = dynamic(
          () => import('shop/Shop'),
          {
            ssr: false,
            loading: () => <p>加载商城模块...</p>
          }
        )

        const RemoteBlog = dynamic(
          () => import('blog/Blog'),
          {
            ssr: false,
            loading: () => <p>加载博客模块...</p>
          }
        )

        export default function Home() {
          return (
            <div>
              <h1>主应用</h1>
              <RemoteShop />
              <RemoteBlog />
            </div>
          )
        }
        """, language="javascript")

with micro_col2:
    with st.expander("微前端路由", expanded=True):
        st.code("""
        // lib/router.js
        class MicroFrontendRouter {
          constructor() {
            this.routes = new Map()
            this.defaultRoute = null
          }
  
          register(prefix, app) {
            this.routes.set(prefix, app)
          }
  
          setDefault(app) {
            this.defaultRoute = app
          }
  
          async resolve(path) {
            for (const [prefix, app] of this.routes) {
              if (path.startsWith(prefix)) {
                return app
              }
            }
            return this.defaultRoute
          }
        }

        // pages/_app.js
        import { MicroFrontendRouter } from '../lib/router'

        const router = new MicroFrontendRouter()

        router.register('/shop', {
          module: () => import('shop/App'),
          name: 'shop'
        })

        router.register('/blog', {
          module: () => import('blog/App'),
          name: 'blog'
        })

        router.setDefault({
          module: () => import('../components/Home'),
          name: 'home'
        })

        export default function App({ Component, pageProps, router }) {
          const [MicroFrontend, setMicroFrontend] = useState(null)
  
          useEffect(() => {
            const loadMicroFrontend = async () => {
              const app = await router.resolve(router.pathname)
              const MicroApp = await app.module()
              setMicroFrontend(() => MicroApp)
            }
    
            loadMicroFrontend()
          }, [router.pathname])
  
          if (MicroFrontend) {
            return <MicroFrontend {...pageProps} />
          }
  
          return <Component {...pageProps} />
        }
        """, language="javascript")



# 添加持续集成/部署
st.header("持续集成/部署 (CI/CD)")

cicd_col1, cicd_col2 = st.columns(2)

with cicd_col1:
    with st.expander("GitHub Actions", expanded=True):
        st.code("""
        # .github/workflows/ci.yml
        name: CI/CD

        on:
          push:
            branches: [ main ]
          pull_request:
            branches: [ main ]

        jobs:
          test:
            runs-on: ubuntu-latest
            
            steps:
              - uses: actions/checkout@v3
              
              - name: Setup Node.js
                uses: actions/setup-node@v3
                with:
                  node-version: '18'
                  cache: 'npm'
                  
              - name: Install dependencies
                run: npm ci
                
              - name: Run linter
                run: npm run lint
                
              - name: Run tests
                run: npm test
                
              - name: Build application
                run: npm run build

          deploy:
            needs: test
            runs-on: ubuntu-latest
            if: github.ref == 'refs/heads/main'
            
            steps:
              - name: Deploy to Vercel
                uses: amondnet/vercel-action@v20
                with:
                  vercel-token: ${{ secrets.VERCEL_TOKEN }}
                  vercel-org-id: ${{ secrets.ORG_ID}}
                  vercel-project-id: ${{ secrets.PROJECT_ID }}
                  vercel-args: '--prod'
        """, language="yaml")

with cicd_col2:
    with st.expander("部署配置", expanded=True):
        st.code("""
        // vercel.json
        {
          "version": 2,
          "builds": [
            {
              "src": "package.json",
              "use": "@vercel/next"
            }
          ],
          "routes": [
            {
              "src": "/api/(.*)",
              "headers": {
                "cache-control": "public, max-age=0, must-revalidate"
              }
            }
          ],
          "env": {
            "DATABASE_URL": "@database-url",
            "REDIS_URL": "@redis-url",
            "API_KEY": "@api-key"
          }
        }

        // next.config.js
        module.exports = {
          // 生产环境优化
          productionBrowserSourceMaps: false,
          compress: true,
          generateEtags: true,
          poweredByHeader: false,
          
          // 构建输出
          output: 'standalone',
          
          // 环境变量
          env: {
            API_URL: process.env.API_URL
          },
          
          // 构建优化
          experimental: {
            optimizeCss: true,
            scrollRestoration: true,
            workerThreads: true,
            optimizeImages: true
          }
        }
        """, language="javascript")

# 添加性能优化最佳实践
st.header("性能优化最佳实践")

perf_col1, perf_col2 = st.columns(2)

with perf_col1:
    with st.expander("代码分割", expanded=True):
        st.code("""
        // components/DynamicComponent.js
        import dynamic from 'next/dynamic'

        // 动态导入组件
        const DynamicChart = dynamic(
          () => import('../components/Chart'),
          {
            loading: () => <p>加载中...</p>,
            ssr: false
          }
        )

        // 动态导入库
        const moment = dynamic(
          () => import('moment'),
          { ssr: false }
        )

        // 路由级别代码分割
        const routes = {
          '/dashboard': dynamic(() => import('../pages/dashboard')),
          '/profile': dynamic(() => import('../pages/profile')),
          '/settings': dynamic(() => import('../pages/settings'))
        }

        // 条件加载
        const AdminPanel = dynamic(
          () => import('../components/AdminPanel'),
          {
            loading: () => <p>加载管理面板...</p>,
            ssr: false,
            // 仅在需要时加载
            loading: ({ error, isLoading }) => {
              if (error) return <div>加载失败</div>
              if (isLoading) return <div>加载中...</div>
              return null
            }
          }
        )
        """, language="javascript")

with perf_col2:
    with st.expander("资源优化", expanded=True):
        st.code("""
        // next.config.js
        module.exports = {
          // 图片优化
          images: {
            domains: ['assets.example.com'],
            deviceSizes: [640, 750, 828, 1080, 1200],
            imageSizes: [16, 32, 48, 64, 96],
            formats: ['image/avif', 'image/webp']
          },
          
          // 字体优化
          optimizeFonts: true,
          
          // webpack配置
          webpack: (config, { dev, isServer }) => {
            // 生产环境优化
            if (!dev && !isServer) {
              config.optimization.splitChunks = {
                chunks: 'all',
                minSize: 20000,
                maxSize: 244000,
                minChunks: 1,
                maxAsyncRequests: 30,
                maxInitialRequests: 30,
                cacheGroups: {
                  default: false,
                  vendors: false,
                  framework: {
                    chunks: 'all',
                    name: 'framework',
                    test: /[\\/]node_modules[\\/]/,
                    priority: 40,
                    enforce: true
                  },
                  lib: {
                    test: /[\\/]node_modules[\\/]/,
                    priority: 30,
                    minChunks: 2,
                    reuseExistingChunk: true
                  }
                }
              }
            }
            return config
          }
        }

        // components/OptimizedImage.js
        import Image from 'next/image'

        export function OptimizedImage({ src, alt, ...props }) {
          return (
            <div className="image-container">
              <Image
                src={src}
                alt={alt}
                placeholder="blur"
                loading="lazy"
                quality={75}
                {...props}
              />
            </div>
          )
        }
        """, language="javascript")
        


# 添加调试和开发工具
st.header("调试和开发工具")

debug_col1, debug_col2 = st.columns(2)

with debug_col1:
    with st.expander("调试配置", expanded=True):
        st.code("""
        // .vscode/launch.json
        {
          "version": "0.2.0",
          "configurations": [
            {
              "type": "node",
              "request": "launch",
              "name": "Next.js: Debug Server",
              "program": "${workspaceFolder}/node_modules/next/dist/bin/next",
              "args": ["dev"],
              "env": {
                "NODE_OPTIONS": "--inspect"
              },
              "console": "integratedTerminal"
            },
            {
              "type": "chrome",
              "request": "launch",
              "name": "Next.js: Debug Client",
              "url": "http://localhost:3000",
              "webRoot": "${workspaceFolder}"
            }
          ]
        }

        // utils/debug.js
        export const debug = (namespace) => {
          return (...args) => {
            if (process.env.NODE_ENV === 'development') {
              console.log(`[${namespace}]`, ...args)
            }
          }
        }

        // 使用示例
        const log = debug('UserProfile')
        log('用户数据加载中...', userData)
        """, language="javascript")

with debug_col2:
    with st.expander("开发工具", expanded=True):
        st.code("""
        // middleware/logger.js
        export function devLogger(req, res, next) {
          if (process.env.NODE_ENV === 'development') {
            const start = Date.now()
            
            res.on('finish', () => {
              const duration = Date.now() - start
              console.log(`
                📝 ${req.method} ${req.url}
                ⏱️  ${duration}ms
                📊 ${res.statusCode}
                🔄 ${res.get('Content-Length') || 0}b
              `)
            })
          }
          
          next()
        }

        // components/DevTools.js
        export function DevTools({ children }) {
          if (process.env.NODE_ENV !== 'development') {
            return children
          }

          return (
            <>
              {children}
              <div className="fixed bottom-0 right-0 p-4 bg-black text-white">
                <div>🔍 开发工具</div>
                <div>
                  <button onClick={() => localStorage.clear()}>
                    清除存储
                  </button>
                  <button onClick={() => window.location.reload()}>
                    刷新页面
                  </button>
                </div>
              </div>
            </>
          )
        }
        """, language="javascript")

# 添加测试策略
st.header("测试策略")

test_col1, test_col2 = st.columns(2)

with test_col1:
    with st.expander("单元测试", expanded=True):
        st.code("""
        // __tests__/components/Button.test.tsx
        import { render, fireEvent } from '@testing-library/react'
        import { Button } from '@/components/Button'

        describe('Button Component', () => {
          it('renders correctly', () => {
            const { getByText } = render(
              <Button>Click me</Button>
            )
            
            expect(getByText('Click me')).toBeInTheDocument()
          })

          it('handles click events', () => {
            const handleClick = jest.fn()
            const { getByText } = render(
              <Button onClick={handleClick}>Click me</Button>
            )
            
            fireEvent.click(getByText('Click me'))
            expect(handleClick).toHaveBeenCalledTimes(1)
          })

          it('can be disabled', () => {
            const { getByText } = render(
              <Button disabled>Click me</Button>
            )
            
            expect(getByText('Click me')).toBeDisabled()
          })
        })

        // __tests__/hooks/useAuth.test.ts
        import { renderHook, act } from '@testing-library/react-hooks'
        import { useAuth } from '@/hooks/useAuth'

        describe('useAuth Hook', () => {
          it('handles login', async () => {
            const { result } = renderHook(() => useAuth())
            
            await act(async () => {
              await result.current.login({
                email: 'test@example.com',
                password: 'password'
              })
            })
            
            expect(result.current.user).toBeTruthy()
            expect(result.current.isAuthenticated).toBe(true)
          })
        })
        """, language="typescript")

with test_col2:
    with st.expander("集成测试", expanded=True):
        st.code("""
        // cypress/integration/auth.spec.ts
        describe('Authentication', () => {
          beforeEach(() => {
            cy.visit('/login')
          })

          it('should login successfully', () => {
            cy.get('input[name="email"]')
              .type('user@example.com')
            
            cy.get('input[name="password"]')
              .type('password123')
            
            cy.get('button[type="submit"]')
              .click()
            
            cy.url().should('include', '/dashboard')
            cy.get('[data-testid="user-menu"]')
              .should('be.visible')
          })

          it('should show error for invalid credentials', () => {
            cy.get('input[name="email"]')
              .type('invalid@example.com')
            
            cy.get('input[name="password"]')
              .type('wrongpassword')
            
            cy.get('button[type="submit"]')
              .click()
            
            cy.get('[data-testid="error-message"]')
              .should('be.visible')
              .and('contain', '无效的凭据')
          })
        })

        // jest.config.js
        module.exports = {
          testEnvironment: 'jsdom',
          setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
          testPathIgnorePatterns: [
            '<rootDir>/.next/',
            '<rootDir>/node_modules/'
          ],
          moduleNameMapper: {
            '^@/components/(.*)$': '<rootDir>/components/$1',
            '^@/pages/(.*)$': '<rootDir>/pages/$1'
          },
          transform: {
            '^.+\\.(js|jsx|ts|tsx)$': ['babel-jest', { presets: ['next/babel'] }]
          },
          collectCoverageFrom: [
            '**/*.{js,jsx,ts,tsx}',
            '!**/*.d.ts',
            '!**/node_modules/**'
          ]
        }
        """, language="javascript")




# 保持前面的代码不变...

# 添加安全最佳实践
st.header("安全最佳实践")

security_col1, security_col2 = st.columns(2)

with security_col1:
    with st.expander("安全中间件", expanded=True):
        st.code("""
        // middleware/security.js
        import { NextResponse } from 'next/server'

        export function middleware(request) {
          const response = NextResponse.next()
          
          // 基础安全头部
          response.headers.set('X-XSS-Protection', '1; mode=block')
          response.headers.set('X-Frame-Options', 'DENY')
          response.headers.set('X-Content-Type-Options', 'nosniff')
          response.headers.set(
            'Strict-Transport-Security',
            'max-age=31536000; includeSubDomains'
          )
          
          // 内容安全策略
          response.headers.set(
            'Content-Security-Policy',
            `
              default-src 'self';
              script-src 'self' 'unsafe-inline' 'unsafe-eval';
              style-src 'self' 'unsafe-inline';
              img-src 'self' data: https:;
              font-src 'self';
            `.replace(/\\s+/g, ' ').trim()
          )
          
          return response
        }

        export const config = {
          matcher: [
            '/((?!api|_next/static|favicon.ico).*)',
          ],
        }
        """, language="javascript")

with security_col2:
    with st.expander("认证与授权", expanded=True):
        st.code("""
        // lib/auth.js
        import { getSession } from 'next-auth/react'
        import { verify } from 'jsonwebtoken'

        export async function authenticateUser(req) {
          try {
            const token = req.headers.authorization?.split(' ')[1]
            if (!token) throw new Error('No token provided')
            
            const decoded = verify(token, process.env.JWT_SECRET)
            return decoded
          } catch (error) {
            throw new Error('Authentication failed')
          }
        }

        export function withAuth(handler) {
          return async (req, res) => {
            try {
              const session = await getSession({ req })
              if (!session) {
                return res.status(401).json({ 
                  error: 'Unauthorized' 
                })
              }
              
              // 添加用户信息到请求
              req.user = session.user
              return handler(req, res)
            } catch (error) {
              return res.status(401).json({ 
                error: 'Authentication failed' 
              })
            }
          }
        }

        // 基于角色的访问控制
        export function withRole(roles) {
          return (handler) => {
            return async (req, res) => {
              try {
                const session = await getSession({ req })
                if (!session) {
                  return res.status(401).json({ 
                    error: 'Unauthorized' 
                  })
                }
                
                const hasRole = roles.some(
                  role => session.user.roles.includes(role)
                )
                
                if (!hasRole) {
                  return res.status(403).json({ 
                    error: 'Forbidden' 
                  })
                }
                
                return handler(req, res)
              } catch (error) {
                return res.status(401).json({ 
                  error: 'Authentication failed' 
                })
              }
            }
          }
        }
        """, language="javascript")

# 添加错误处理
st.header("错误处理")

error_col1, error_col2 = st.columns(2)

with error_col1:
    with st.expander("全局错误处理", expanded=True):
        st.code("""
        // lib/errors.js
        export class AppError extends Error {
          constructor(message, statusCode = 500) {
            super(message)
            this.statusCode = statusCode
            this.status = `${statusCode}`.startsWith('4') ? 'fail' : 'error'
            this.isOperational = true
            
            Error.captureStackTrace(this, this.constructor)
          }
        }

        // pages/_app.js
        import { ErrorBoundary } from 'react-error-boundary'

        function ErrorFallback({ error, resetErrorBoundary }) {
          return (
            <div role="alert">
              <h2>出错了！</h2>
              <pre>{error.message}</pre>
              <button onClick={resetErrorBoundary}>
                重试
              </button>
            </div>
          )
        }

        export default function App({ Component, pageProps }) {
          return (
            <ErrorBoundary
              FallbackComponent={ErrorFallback}
              onReset={() => {
                // 重置应用状态
              }}
            >
              <Component {...pageProps} />
            </ErrorBoundary>
          )
        }

        // 自定义错误页面
        // pages/404.js
        export default function Custom404() {
          return (
            <div>
              <h1>404 - 页面未找到</h1>
              <p>抱歉，您访问的页面不存在。</p>
            </div>
          )
        }

        // pages/500.js
        export default function Custom500() {
          return (
            <div>
              <h1>500 - 服务器错误</h1>
              <p>抱歉，服务器出现了问题。</p>
            </div>
          )
        }
        """, language="javascript")

with error_col2:
    with st.expander("API 错误处理", expanded=True):
        st.code("""
        // lib/api-error.js
        export class APIError extends Error {
          constructor(statusCode, message, errors = []) {
            super(message)
            this.statusCode = statusCode
            this.errors = errors
          }
        }

        export function withErrorHandler(handler) {
          return async (req, res) => {
            try {
              await handler(req, res)
            } catch (error) {
              console.error(error)
              
              if (error instanceof APIError) {
                return res.status(error.statusCode).json({
                  status: 'error',
                  message: error.message,
                  errors: error.errors
                })
              }
              
              return res.status(500).json({
                status: 'error',
                message: '服务器内部错误'
              })
            }
          }
        }

        // pages/api/example.js
        import { APIError, withErrorHandler } from '../../lib/api-error'

        async function handler(req, res) {
          if (!req.body.name) {
            throw new APIError(400, '缺少必要参数', [{
              field: 'name',
              message: '名称是必需的'
            }])
          }
          
          try {
            const result = await someOperation()
            res.json(result)
          } catch (error) {
            throw new APIError(500, '操作失败')
          }
        }

        export default withErrorHandler(handler)
        """, language="javascript")



# 添加监控方案
st.header("监控方案")

monitor_col1, monitor_col2 = st.columns(2)

with monitor_col1:
    with st.expander("性能监控", expanded=True):
        st.code("""
        // lib/monitoring.js
        import * as Sentry from '@sentry/nextjs'

        export function initMonitoring() {
          Sentry.init({
            dsn: process.env.SENTRY_DSN,
            tracesSampleRate: 1.0,
            environment: process.env.NODE_ENV,
            integrations: [
              new Sentry.BrowserTracing({
                traceFetch: true,
                traceXHR: true,
              }),
            ],
          })
        }

        // 性能指标监控
        export function reportWebVitals(metric) {
          switch (metric.name) {
            case 'FCP':
              // 首次内容绘制
              logMetric('FCP', metric.value)
              break
            case 'LCP':
              // 最大内容绘制
              logMetric('LCP', metric.value)
              break
            case 'CLS':
              // 累积布局偏移
              logMetric('CLS', metric.value)
              break
            case 'FID':
              // 首次输入延迟
              logMetric('FID', metric.value)
              break
            case 'TTFB':
              // 首字节时间
              logMetric('TTFB', metric.value)
              break
          }
        }

        // 自定义性能监控
        export function measurePerformance(name, fn) {
          const start = performance.now()
          const result = fn()
          const duration = performance.now() - start
          
          logMetric(name, duration)
          return result
        }
        """, language="javascript")

with monitor_col2:
    with st.expander("错误监控", expanded=True):
        st.code("""
        // lib/error-tracking.js
        export class ErrorTracker {
          constructor() {
            this.errors = []
            this.maxErrors = 100
            
            window.addEventListener('error', this.handleError)
            window.addEventListener('unhandledrejection', this.handlePromiseError)
          }

          handleError = (event) => {
            this.trackError({
              type: 'runtime',
              message: event.message,
              stack: event.error?.stack,
              location: {
                filename: event.filename,
                line: event.lineno,
                column: event.colno
              }
            })
          }

          handlePromiseError = (event) => {
            this.trackError({
              type: 'promise',
              message: event.reason?.message || 'Promise rejected',
              stack: event.reason?.stack
            })
          }

          trackError(error) {
            this.errors.push({
              ...error,
              timestamp: new Date().toISOString(),
              url: window.location.href,
              userAgent: navigator.userAgent
            })

            if (this.errors.length > this.maxErrors) {
              this.errors.shift()
            }

            // 发送到监控服务
            this.sendToMonitoringService(error)
          }

          async sendToMonitoringService(error) {
            try {
              await fetch('/api/monitoring/error', {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify(error)
              })
            } catch (e) {
              console.error('Failed to send error to monitoring service:', e)
            }
          }
        }

        // 使用示例
        const errorTracker = new ErrorTracker()
        """, language="javascript")

# 添加 API 集成
st.header("API 集成")

api_col1, api_col2 = st.columns(2)

with api_col1:
    with st.expander("API 客户端", expanded=True):
        st.code("""
        // lib/api-client.js
        export class APIClient {
          constructor(baseURL) {
            this.baseURL = baseURL
            this.token = null
          }

          setToken(token) {
            this.token = token
          }

          async request(method, path, data = null) {
            const url = `${this.baseURL}${path}`
            const headers = {
              'Content-Type': 'application/json'
            }

            if (this.token) {
              headers['Authorization'] = `Bearer ${this.token}`
            }

            try {
              const response = await fetch(url, {
                method,
                headers,
                body: data ? JSON.stringify(data) : null
              })

              if (!response.ok) {
                throw await this.handleError(response)
              }

              return await response.json()
            } catch (error) {
              throw error
            }
          }

          async handleError(response) {
            const error = await response.json()
            throw new APIError(
              response.status,
              error.message || '请求失败',
              error.errors
            )
          }

          // REST 方法
          get(path) {
            return this.request('GET', path)
          }

          post(path, data) {
            return this.request('POST', path, data)
          }

          put(path, data) {
            return this.request('PUT', path, data)
          }

          delete(path) {
            return this.request('DELETE', path)
          }
        }
        """, language="javascript")

with api_col2:
    with st.expander("API Hooks", expanded=True):
        st.code("""
        // hooks/useAPI.js
        import useSWR from 'swr'
import { APIClient } from '../lib/api-client'

const client = new APIClient(process.env.NEXT_PUBLIC_API_URL)

export function useAPI(path, options = {}) {
  const { data, error, mutate } = useSWR(
    path,
    () => client.get(path),
    {
      revalidateOnFocus: false,
      ...options
    }
  )

  return {
    data,
    error,
    loading: !data && !error,
    mutate
  }
}

export function useMutation(path, method = 'POST') {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const mutate = async (data) => {
    try {
      setLoading(true)
      setError(null)
      
      const result = await client[method.toLowerCase()](path, data)
      return result
    } catch (err) {
      setError(err)
      throw err
    } finally {
      setLoading(false)
    }
  }

  return {
    mutate,
    loading,
    error
  }
}

// 使用示例
function UserProfile({ userId }) {
  const { data, loading, error } = useAPI(`/users/${userId}`)
  const { mutate: updateUser, loading: updating } = useMutation(
    `/users/${userId}`,
    'PUT'
  )

  if (loading) return <div>加载中...</div>
  if (error) return <div>加载失败</div>

  return (
    <div>
      <h1>{data.name}</h1>
      <button 
        onClick={() => updateUser({ name: 'New Name' })}
        disabled={updating}
      >
        更新用户
      </button>
    </div>
  )
}
        """, language="javascript")


# 添加监控方案
st.header("监控方案")

monitor_col1, monitor_col2 = st.columns(2)

with monitor_col1:
    with st.expander("性能监控", expanded=True):
        st.code("""
        // lib/monitoring.js
        import * as Sentry from '@sentry/nextjs'

        export function initMonitoring() {
          Sentry.init({
            dsn: process.env.SENTRY_DSN,
            tracesSampleRate: 1.0,
            environment: process.env.NODE_ENV,
            integrations: [
              new Sentry.BrowserTracing({
                traceFetch: true,
                traceXHR: true,
              }),
            ],
          })
        }

        // 性能指标监控
        export function reportWebVitals(metric) {
          switch (metric.name) {
            case 'FCP':
              // 首次内容绘制
              logMetric('FCP', metric.value)
              break
            case 'LCP':
              // 最大内容绘制
              logMetric('LCP', metric.value)
              break
            case 'CLS':
              // 累积布局偏移
              logMetric('CLS', metric.value)
              break
            case 'FID':
              // 首次输入延迟
              logMetric('FID', metric.value)
              break
            case 'TTFB':
              // 首字节时间
              logMetric('TTFB', metric.value)
              break
          }
        }

        // 自定义性能监控
        export function measurePerformance(name, fn) {
          const start = performance.now()
          const result = fn()
          const duration = performance.now() - start
          
          logMetric(name, duration)
          return result
        }
        """, language="javascript")

with monitor_col2:
    with st.expander("错误监控", expanded=True):
        st.code("""
        // lib/error-tracking.js
        export class ErrorTracker {
          constructor() {
            this.errors = []
            this.maxErrors = 100
            
            window.addEventListener('error', this.handleError)
            window.addEventListener('unhandledrejection', this.handlePromiseError)
          }

          handleError = (event) => {
            this.trackError({
              type: 'runtime',
              message: event.message,
              stack: event.error?.stack,
              location: {
                filename: event.filename,
                line: event.lineno,
                column: event.colno
              }
            })
          }

          handlePromiseError = (event) => {
            this.trackError({
              type: 'promise',
              message: event.reason?.message || 'Promise rejected',
              stack: event.reason?.stack
            })
          }

          trackError(error) {
            this.errors.push({
              ...error,
              timestamp: new Date().toISOString(),
              url: window.location.href,
              userAgent: navigator.userAgent
            })

            if (this.errors.length > this.maxErrors) {
              this.errors.shift()
            }

            // 发送到监控服务
            this.sendToMonitoringService(error)
          }

          async sendToMonitoringService(error) {
            try {
              await fetch('/api/monitoring/error', {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify(error)
              })
            } catch (e) {
              console.error('Failed to send error to monitoring service:', e)
            }
          }
        }

        // 使用示例
        const errorTracker = new ErrorTracker()
        """, language="javascript")

# 添加 API 集成
st.header("API 集成")

api_col1, api_col2 = st.columns(2)

with api_col1:
    with st.expander("API 客户端", expanded=True):
        st.code("""
        // lib/api-client.js
        export class APIClient {
          constructor(baseURL) {
            this.baseURL = baseURL
            this.token = null
          }

          setToken(token) {
            this.token = token
          }

          async request(method, path, data = null) {
            const url = `${this.baseURL}${path}`
            const headers = {
              'Content-Type': 'application/json'
            }

            if (this.token) {
              headers['Authorization'] = `Bearer ${this.token}`
            }

            try {
              const response = await fetch(url, {
                method,
                headers,
                body: data ? JSON.stringify(data) : null
              })

              if (!response.ok) {
                throw await this.handleError(response)
              }

              return await response.json()
            } catch (error) {
              throw error
            }
          }

          async handleError(response) {
            const error = await response.json()
            throw new APIError(
              response.status,
              error.message || '请求失败',
              error.errors
            )
          }

          // REST 方法
          get(path) {
            return this.request('GET', path)
          }

          post(path, data) {
            return this.request('POST', path, data)
          }

          put(path, data) {
            return this.request('PUT', path, data)
          }

          delete(path) {
            return this.request('DELETE', path)
          }
        }
        """, language="javascript")

with api_col2:
    with st.expander("API Hooks", expanded=True):
        st.code("""
        // hooks/useAPI.js
        import useSWR from 'swr'
import { APIClient } from '../lib/api-client'

const client = new APIClient(process.env.NEXT_PUBLIC_API_URL)

export function useAPI(path, options = {}) {
  const { data, error, mutate } = useSWR(
    path,
    () => client.get(path),
    {
      revalidateOnFocus: false,
      ...options
    }
  )

  return {
    data,
    error,
    loading: !data && !error,
    mutate
  }
}

export function useMutation(path, method = 'POST') {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const mutate = async (data) => {
    try {
      setLoading(true)
      setError(null)
      
      const result = await client[method.toLowerCase()](path, data)
      return result
    } catch (err) {
      setError(err)
      throw err
    } finally {
      setLoading(false)
    }
  }

  return {
    mutate,
    loading,
    error
  }
}

// 使用示例
function UserProfile({ userId }) {
  const { data, loading, error } = useAPI(`/users/${userId}`)
  const { mutate: updateUser, loading: updating } = useMutation(
    `/users/${userId}`,
    'PUT'
  )

  if (loading) return <div>加载中...</div>
  if (error) return <div>加载失败</div>

  return (
    <div>
      <h1>{data.name}</h1>
      <button 
        onClick={() => updateUser({ name: 'New Name' })}
        disabled={updating}
      >
        更新用户
      </button>
    </div>
  )
}
        """, language="javascript")
        

# 保持前面的代码不变...

# 添加数据管理
st.header("数据管理")

data_col1, data_col2 = st.columns(2)

with data_col1:
    with st.expander("状态管理", expanded=True):
        st.code("""
        // store/index.js
        import create from 'zustand'
        import { persist } from 'zustand/middleware'

        export const useStore = create(
          persist(
            (set, get) => ({
              // 用户状态
              user: null,
              setUser: (user) => set({ user }),
              clearUser: () => set({ user: null }),
              
              // 主题状态
              theme: 'light',
              setTheme: (theme) => set({ theme }),
              
              // 购物车状态
              cart: [],
              addToCart: (product) => set((state) => ({
                cart: [...state.cart, product]
              })),
              removeFromCart: (productId) => set((state) => ({
                cart: state.cart.filter(item => item.id !== productId)
              })),
              clearCart: () => set({ cart: [] }),
              
              // 计算属性
              get cartTotal() {
                return get().cart.reduce(
                  (total, item) => total + item.price,
                  0
                )
              }
            }),
            {
              name: 'app-storage',
              getStorage: () => localStorage
            }
          )
        )

        // hooks/useData.js
        import { useStore } from '../store'
        import { useQuery, useMutation, useQueryClient } from 'react-query'

        export function useData(key, fetcher, options = {}) {
          const queryClient = useQueryClient()
          
          const query = useQuery(key, fetcher, {
            staleTime: 1000 * 60 * 5, // 5分钟
            cacheTime: 1000 * 60 * 30, // 30分钟
            ...options
          })
          
          const mutation = useMutation(
            (data) => updateData(key, data),
            {
              onSuccess: () => {
                queryClient.invalidateQueries(key)
              }
            }
          )
          
          return {
            ...query,
            update: mutation.mutate
          }
        }
        """, language="javascript")

with data_col2:
    with st.expander("数据缓存", expanded=True):
        st.code("""
        // lib/cache-manager.js
        class CacheManager {
          constructor() {
            this.cache = new Map()
            this.maxAge = 1000 * 60 * 5 // 5分钟
          }
          
          set(key, value, ttl = this.maxAge) {
            this.cache.set(key, {
              value,
              expires: Date.now() + ttl
            })
          }
          
          get(key) {
            const item = this.cache.get(key)
            if (!item) return null
            
            if (Date.now() > item.expires) {
              this.cache.delete(key)
              return null
            }
            
            return item.value
          }
          
          clear() {
            this.cache.clear()
          }
          
          cleanup() {
            for (const [key, item] of this.cache.entries()) {
              if (Date.now() > item.expires) {
                this.cache.delete(key)
              }
            }
          }
        }

        export const cacheManager = new CacheManager()

        // hooks/useCachedData.js
        export function useCachedData(key, fetcher) {
          const [data, setData] = useState(null)
          const [loading, setLoading] = useState(true)
          
          useEffect(() => {
            const loadData = async () => {
              // 检查缓存
              const cached = cacheManager.get(key)
              if (cached) {
                setData(cached)
                setLoading(false)
                return
              }
              
              // 获取新数据
              try {
                const fresh = await fetcher()
                cacheManager.set(key, fresh)
                setData(fresh)
              } finally {
                setLoading(false)
              }
            }
            
            loadData()
          }, [key])
          
          return { data, loading }
        }
        """, language="javascript")

# 添加主题系统
st.header("主题系统")

theme_col1, theme_col2 = st.columns(2)

with theme_col1:
    with st.expander("主题配置", expanded=True):
        st.code("""
        // styles/theme.js
        export const themes = {
          light: {
            colors: {
              primary: '#007AFF',
              secondary: '#5856D6',
              background: '#FFFFFF',
              text: '#000000',
              border: '#E5E5EA',
              error: '#FF3B30',
              success: '#34C759'
            },
            spacing: {
              xs: '0.25rem',
              sm: '0.5rem',
              md: '1rem',
              lg: '1.5rem',
              xl: '2rem'
            },
            typography: {
              h1: {
                fontSize: '2.5rem',
                fontWeight: 'bold',
                lineHeight: 1.2
              },
              body: {
                fontSize: '1rem',
                lineHeight: 1.5
              }
            },
            shadows: {
              sm: '0 1px 3px rgba(0,0,0,0.12)',
              md: '0 4px 6px rgba(0,0,0,0.1)',
              lg: '0 10px 15px rgba(0,0,0,0.1)'
            },
            transitions: {
              fast: '150ms ease',
              normal: '300ms ease',
              slow: '500ms ease'
            }
          },
          dark: {
            colors: {
              primary: '#0A84FF',
              secondary: '#5E5CE6',
              background: '#000000',
              text: '#FFFFFF',
              border: '#38383A',
              error: '#FF453A',
              success: '#32D74B'
            },
            // 继承其他属性...
          }
        }

        // context/ThemeContext.js
        import { createContext, useContext, useState } from 'react'
        import { themes } from '../styles/theme'

        const ThemeContext = createContext()

        export function ThemeProvider({ children }) {
          const [theme, setTheme] = useState('light')
          
          const toggleTheme = () => {
            setTheme(current => 
              current === 'light' ? 'dark' : 'light'
            )
          }
          
          return (
            <ThemeContext.Provider 
              value={{
                theme: themes[theme],
                currentTheme: theme,
                toggleTheme
              }}
            >
              {children}
            </ThemeContext.Provider>
          )
        }

        export const useTheme = () => useContext(ThemeContext)
        """, language="javascript")

with theme_col2:
    with st.expander("主题组件", expanded=True):
        st.code("""
        // components/ThemeToggle.js
        import { useTheme } from '../context/ThemeContext'

        export function ThemeToggle() {
          const { currentTheme, toggleTheme } = useTheme()
          
          return (
            <button onClick={toggleTheme}>
              {currentTheme === 'light' ? '🌙' : '☀️'}
            </button>
          )
        }

        // components/styled/Button.js
        import styled from 'styled-components'

        export const Button = styled.button`
          background: ${({ theme }) => theme.colors.primary};
          color: ${({ theme }) => theme.colors.text};
          padding: ${({ theme }) => `
            ${theme.spacing.sm} ${theme.spacing.md}
          `};
          border-radius: 4px;
          border: none;
          transition: ${({ theme }) => theme.transitions.fast};
          
          &:hover {
            opacity: 0.9;
            transform: translateY(-1px);
          }
          
          &:disabled {
            opacity: 0.5;
            cursor: not-allowed;
          }
`

        // components/ThemeAwareComponent.js
        import { useTheme } from '../context/ThemeContext'

        export function ThemeAwareComponent() {
          const { theme } = useTheme()
          
          return (
            <div style={{
              background: theme.colors.background,
              color: theme.colors.text,
              padding: theme.spacing.md,
              boxShadow: theme.shadows.md
            }}>
              <h1 style={{
                ...theme.typography.h1,
                marginBottom: theme.spacing.md
              }}>
                主题感知组件
              </h1>
              <p style={theme.typography.body}>
                这个组件会根据当前主题自动调整样式
              </p>
            </div>
          )
        }
        """, language="javascript")

# 添加表单处理
st.header("表单处理")

form_col1, form_col2 = st.columns(2)

with form_col1:
    with st.expander("表单组件", expanded=True):
        st.code("""
        // components/Form/index.js
        import { useForm } from 'react-hook-form'
        import { zodResolver } from '@hookform/resolvers/zod'
        import * as z from 'zod'

        // 表单验证模式
        const schema = z.object({
          username: z.string()
            .min(3, '用户名至少3个字符')
            .max(20, '用户名最多20个字符'),
          email: z.string()
            .email('请输入有效的邮箱地址'),
          password: z.string()
            .min(8, '密码至少8个字符')
            .regex(
              /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/,
              '密码必须包含大小写字母和数字'
            ),
          confirmPassword: z.string()
        }).refine(
          (data) => data.password === data.confirmPassword,
          {
            message: '两次输入的密码不一致',
            path: ['confirmPassword']
          }
        )

        export function Form({ onSubmit, children, ...props }) {
          const {
            register,
            handleSubmit,
            formState: { errors, isSubmitting },
            reset
          } = useForm({
            resolver: zodResolver(schema)
          })

          const handleFormSubmit = async (data) => {
            try {
              await onSubmit(data)
              reset()
            } catch (error) {
              console.error('Form submission error:', error)
            }
          }

          return (
            <form 
              onSubmit={handleSubmit(handleFormSubmit)}
              {...props}
            >
              {typeof children === 'function'
                ? children({ register, errors, isSubmitting })
                : children
              }
            </form>
          )
        }

        // 使用示例
        function RegistrationForm() {
          return (
            <Form onSubmit={async (data) => {
              await registerUser(data)
            }}>
              {({ register, errors, isSubmitting }) => (
                <>
                  <Input
                    {...register('username')}
                    error={errors.username?.message}
                  />
                  <Input
                    {...register('email')}
                    error={errors.email?.message}
                  />
                  <Input
                    type="password"
                    {...register('password')}
                    error={errors.password?.message}
                  />
                  <Button 
                    type="submit"
                    disabled={isSubmitting}
                  >
                    {isSubmitting ? '提交中...' : '注册'}
                  </Button>
                </>
              )}
            </Form>
          )
        }
        """, language="javascript")

with form_col2:
    with st.expander("表单钩子", expanded=True):
        st.code("""
        // hooks/useFormField.js
        export function useFormField(initialValue = '') {
          const [value, setValue] = useState(initialValue)
          const [touched, setTouched] = useState(false)
          const [error, setError] = useState(null)

          const handleChange = (e) => {
            setValue(e.target.value)
            if (error) validate(e.target.value)
          }

          const handleBlur = () => {
            setTouched(true)
            validate(value)
          }

          const validate = (value) => {
            // 自定义验证逻辑
            setError(null)
          }

          return {
            value,
            touched,
            error,
            onChange: handleChange,
            onBlur: handleBlur
          }
        }

        // hooks/useForm.js
        export function useCustomForm(initialValues = {}) {
          const [values, setValues] = useState(initialValues)
          const [errors, setErrors] = useState({})
          const [touched, setTouched] = useState({})
          const [isSubmitting, setIsSubmitting] = useState(false)

          const handleChange = (name) => (e) => {
            setValues(prev => ({
              ...prev,
              [name]: e.target.value
            }))
          }

          const handleBlur = (name) => () => {
            setTouched(prev => ({
              ...prev,
              [name]: true
            }))
          }

          const handleSubmit = (onSubmit) => async (e) => {
            e.preventDefault()
            setIsSubmitting(true)

            try {
              await onSubmit(values)
            } catch (error) {
              setErrors(error.errors || {})
            } finally {
              setIsSubmitting(false)
            }
          }

          return {
            values,
            errors,
            touched,
            isSubmitting,
            handleChange,
            handleBlur,
            handleSubmit
          }
        }
        """, language="javascript")

# 添加动画系统
st.header("动画系统")

anim_col1, anim_col2 = st.columns(2)

with anim_col1:
    with st.expander("动画组件", expanded=True):
        st.code("""
        // components/Animation/Fade.js
        import { motion, AnimatePresence } from 'framer-motion'

        export function Fade({ 
          children,
          duration = 0.3,
          ...props 
        }) {
          return (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              transition={{ duration }}
              {...props}
            >
              {children}
            </motion.div>
          )
        }

        // components/Animation/Slide.js
        export function Slide({
          children,
          direction = 'right',
          duration = 0.3,
          ...props
        }) {
          const variants = {
            initial: {
              x: direction === 'right' ? -100 : 100,
              opacity: 0
            },
            animate: {
              x: 0,
              opacity: 1
            },
            exit: {
              x: direction === 'right' ? 100 : -100,
              opacity: 0
            }
          }

          return (
            <motion.div
              variants={variants}
              initial="initial"
              animate="animate"
              exit="exit"
              transition={{ duration }}
              {...props}
            >
              {children}
            </motion.div>
          )
        }

        // 使用示例
        function AnimatedPage() {
          return (
            <AnimatePresence>
              <Fade>
                <h1>欢迎!</h1>
              </Fade>
              <Slide direction="right">
                <p>从右侧滑入的内容</p>
              </Slide>
            </AnimatePresence>
          )
        }
        """, language="javascript")

with anim_col2:
    with st.expander("动画钩子", expanded=True):
        st.code("""
        // hooks/useAnimation.js
        import { useSpring, useTransition } from 'react-spring'

        export function useAnimatedValue(
          initialValue,
          config = { tension: 300, friction: 20 }
        ) {
          const [props, set] = useSpring(() => ({
            value: initialValue,
            config
          }))

          const animate = (target) => {
            set({ value: target })
          }

          return [props.value, animate]
        }

        export function useAnimatedList(items) {
          const transitions = useTransition(items, {
            from: { opacity: 0, transform: 'scale(0.8)' },
            enter: { opacity: 1, transform: 'scale(1)' },
            leave: { opacity: 0, transform: 'scale(0.8)' }
          })

          return transitions
        }

        // 使用示例
        function AnimatedCounter({ value }) {
          const [animatedValue, animate] = useAnimatedValue(0)

          useEffect(() => {
            animate(value)
          }, [value])

          return (
            <animated.span>
              {animatedValue.to(v => Math.floor(v))}
            </animated.span>
          )
        }

        function AnimatedList({ items }) {
          const transitions = useAnimatedList(items)

          return transitions((style, item) => (
            <animated.div style={style}>
              {item}
            </animated.div>
          ))
        }
        """, language="javascript")


# 添加微服务集成
st.header("微服务集成")

micro_col1, micro_col2 = st.columns(2)

with micro_col1:
    with st.expander("服务配置", expanded=True):
        st.code("""
        // next.config.js
        const { withModuleFederation } = require('@module-federation/nextjs-mf')

        module.exports = withModuleFederation({
          name: 'host',
          remotes: {
            shop: 'shop@http://localhost:3001/remoteEntry.js',
            blog: 'blog@http://localhost:3002/remoteEntry.js'
          },
          shared: {
            react: {
              singleton: true,
              requiredVersion: false
            },
            'react-dom': {
              singleton: true,
              requiredVersion: false
            }
          }
        })

        // lib/service-registry.js
        class ServiceRegistry {
          constructor() {
            this.services = new Map()
            this.healthChecks = new Map()
          }

          register(name, config) {
            this.services.set(name, {
              url: config.url,
              timeout: config.timeout || 5000,
              retries: config.retries || 3
            })

            if (config.healthCheck) {
              this.healthChecks.set(name, config.healthCheck)
            }
          }

          async getService(name) {
            const service = this.services.get(name)
            if (!service) {
              throw new Error(`Service ${name} not found`)
            }

            // 健康检查
            const healthCheck = this.healthChecks.get(name)
            if (healthCheck) {
              const isHealthy = await healthCheck()
              if (!isHealthy) {
                throw new Error(`Service ${name} is unhealthy`)
              }
            }

            return service
          }

          async call(name, path, options = {}) {
            const service = await this.getService(name)
            const url = `${service.url}${path}`

            return fetch(url, {
              ...options,
              timeout: service.timeout
            })
          }
        }

        export const registry = new ServiceRegistry()
        """, language="javascript")

with micro_col2:
    with st.expander("服务集成", expanded=True):
        st.code("""
        // lib/service-client.js
        class ServiceClient {
          constructor(registry) {
            this.registry = registry
          }

          async request(serviceName, config) {
            let retries = 0
            const service = await this.registry.getService(serviceName)

            while (retries < service.retries) {
              try {
                const response = await this.registry.call(
                  serviceName,
                  config.path,
                  config.options
                )

                if (!response.ok) {
                  throw new Error(`HTTP error! status: ${response.status}`)
                }

                return await response.json()
              } catch (error) {
                retries++
                if (retries === service.retries) {
                  throw error
                }
                // 指数退避
                await new Promise(resolve => 
                  setTimeout(resolve, Math.pow(2, retries) * 100)
                )
              }
            }
          }
        }

        // hooks/useService.js
        export function useService(serviceName, path, options = {}) {
          const [data, setData] = useState(null)
          const [error, setError] = useState(null)
          const [loading, setLoading] = useState(true)

          useEffect(() => {
            const fetchData = async () => {
              try {
                const client = new ServiceClient(registry)
                const result = await client.request(serviceName, {
                  path,
                  options
                })
                setData(result)
              } catch (err) {
                setError(err)
              } finally {
                setLoading(false)
              }
            }

            fetchData()
          }, [serviceName, path])

          return { data, error, loading }
        }
        """, language="javascript")

# 添加权限系统
st.header("权限系统")

auth_col1, auth_col2 = st.columns(2)

with auth_col1:
    with st.expander("权限配置", expanded=True):
        st.code("""
        // lib/permissions.js
        export const PERMISSIONS = {
          USER: {
            READ: 'user:read',
            CREATE: 'user:create',
            UPDATE: 'user:update',
            DELETE: 'user:delete'
          },
          POST: {
            READ: 'post:read',
            CREATE: 'post:create',
            UPDATE: 'post:update',
            DELETE: 'post:delete'
          }
        }

        export class PermissionManager {
          constructor() {
            this.userPermissions = new Set()
            this.rolePermissions = new Map()
          }

          setUserPermissions(permissions) {
            this.userPermissions = new Set(permissions)
          }

          addRolePermissions(role, permissions) {
            this.rolePermissions.set(role, new Set(permissions))
          }

          can(permission) {
            return this.userPermissions.has(permission)
          }

          hasRole(role) {
            return this.rolePermissions.has(role)
          }

          hasAnyRole(roles) {
            return roles.some(role => this.hasRole(role))
          }

          hasAllRoles(roles) {
            return roles.every(role => this.hasRole(role))
          }
        }

        export const permissionManager = new PermissionManager()
        """, language="javascript")

with auth_col2:
    with st.expander("权限组件", expanded=True):
        st.code("""
        // components/Permission.js
        import { usePermissions } from '../hooks/usePermissions'

        export function RequirePermission({ 
          permission,
          fallback = null,
          children 
        }) {
          const { can } = usePermissions()
          
          if (!can(permission)) {
            return fallback
          }
          
          return children
        }

        export function RequireRole({ 
          role,
          fallback = null,
          children 
        }) {
          const { hasRole } = usePermissions()
          
          if (!hasRole(role)) {
            return fallback
          }
          
          return children
        }

        // hooks/usePermissions.js
        import { useContext } from 'react'
        import { PermissionContext } from '../context/PermissionContext'

        export function usePermissions() {
          const context = useContext(PermissionContext)
          
          if (!context) {
            throw new Error(
              'usePermissions must be used within a PermissionProvider'
            )
          }
          
          return context
        }

        // 使用示例
        function AdminPanel() {
          return (
            <RequireRole role="admin" fallback={<AccessDenied />}>
              <div>
                <h1>管理面板</h1>
                <RequirePermission permission={PERMISSIONS.USER.CREATE}>
                  <button>创建用户</button>
                </RequirePermission>
                <RequirePermission permission={PERMISSIONS.USER.DELETE}>
                  <button>删除用户</button>
                </RequirePermission>
              </div>
            </RequireRole>
          )
        }
        """, language="javascript")



# 添加工具函数
st.header("工具函数")

util_col1, util_col2 = st.columns(2)

with util_col1:
    with st.expander("通用工具", expanded=True):
        st.code("""
        // utils/common.js
        export const debounce = (fn, delay) => {
          let timeoutId
          return (...args) => {
            clearTimeout(timeoutId)
            timeoutId = setTimeout(() => fn(...args), delay)
          }
        }

        export const throttle = (fn, limit) => {
          let inThrottle
          return (...args) => {
            if (!inThrottle) {
              fn(...args)
              inThrottle = true
              setTimeout(() => inThrottle = false, limit)
            }
          }
        }

        export const deepClone = (obj) => {
          if (obj === null || typeof obj !== 'object') return obj
          if (obj instanceof Date) return new Date(obj)
          if (obj instanceof Array) return obj.map(item => deepClone(item))
          if (obj instanceof Object) {
            return Object.fromEntries(
              Object.entries(obj).map(([key, value]) => [
                key,
                deepClone(value)
              ])
            )
          }
        }

        export const formatDate = (date, format = 'YYYY-MM-DD') => {
          const d = new Date(date)
          const year = d.getFullYear()
          const month = String(d.getMonth() + 1).padStart(2, '0')
          const day = String(d.getDate()).padStart(2, '0')
          const hours = String(d.getHours()).padStart(2, '0')
          const minutes = String(d.getMinutes()).padStart(2, '0')
          
          return format
            .replace('YYYY', year)
            .replace('MM', month)
            .replace('DD', day)
            .replace('HH', hours)
            .replace('mm', minutes)
        }

        export const queryString = {
          parse: (str) => 
            Object.fromEntries(
              new URLSearchParams(str)
            ),
          stringify: (obj) => 
            new URLSearchParams(obj).toString()
        }
        """, language="javascript")

with util_col2:
    with st.expander("数据处理", expanded=True):
        st.code("""
        // utils/data.js
        export const groupBy = (array, key) => {
          return array.reduce((result, item) => {
            const group = item[key]
            result[group] = result[group] ?? []
            result[group].push(item)
            return result
          }, {})
        }

        export const sortBy = (array, key, order = 'asc') => {
          return [...array].sort((a, b) => {
            const valueA = a[key]
            const valueB = b[key]
            
            if (typeof valueA === 'string') {
              return order === 'asc'
                ? valueA.localeCompare(valueB)
                : valueB.localeCompare(valueA)
            }
            
            return order === 'asc'
              ? valueA - valueB
              : valueB - valueA
          })
        }

        export const filterBy = (array, predicate) => {
          if (typeof predicate === 'function') {
            return array.filter(predicate)
          }
          
          return array.filter(item => 
            Object.entries(predicate).every(([key, value]) =>
              item[key] === value
            )
          )
        }

        export const paginate = (array, page, limit) => {
          const start = (page - 1) * limit
          const end = start + limit
          
          return {
            data: array.slice(start, end),
            total: array.length,
            currentPage: page,
            totalPages: Math.ceil(array.length / limit)
          }
        }
        """, language="javascript")

# 添加测试工具
st.header("测试工具")

test_col1, test_col2 = st.columns(2)

with test_col1:
    with st.expander("测试工具函数", expanded=True):
        st.code("""
        // test/utils.js
        import { render } from '@testing-library/react'
        import { ThemeProvider } from '../context/ThemeContext'
        import { QueryClient, QueryClientProvider } from 'react-query'

        export function renderWithProviders(
          ui,
          {
            theme = 'light',
            queryClient = new QueryClient(),
            ...renderOptions
          } = {}
        ) {
          function Wrapper({ children }) {
            return (
              <QueryClientProvider client={queryClient}>
                <ThemeProvider initialTheme={theme}>
                  {children}
                </ThemeProvider>
              </QueryClientProvider>
            )
          }
          
          return render(ui, { wrapper: Wrapper, ...renderOptions })
        }

        export function createMockRouter(props = {}) {
          return {
            basePath: '',
            pathname: '/',
            route: '/',
            query: {},
            asPath: '/',
            back: jest.fn(),
            beforePopState: jest.fn(),
            prefetch: jest.fn(),
            push: jest.fn(),
            reload: jest.fn(),
            replace: jest.fn(),
            events: {
              on: jest.fn(),
              off: jest.fn(),
              emit: jest.fn()
            },
            isFallback: false,
            isLocaleDomain: false,
            isReady: true,
            ...props
          }
        }

        export function createMockResponse() {
          const res = {
            statusCode: 200,
            status: jest.fn(),
            json: jest.fn(),
            end: jest.fn(),
            setHeader: jest.fn()
          }
          
          res.status.mockReturnValue(res)
          res.json.mockReturnValue(res)
          
          return res
        }
        """, language="javascript")

with test_col2:
    with st.expander("测试钩子", expanded=True):
        st.code("""
        // test/hooks.js
        import { renderHook } from '@testing-library/react-hooks'
        import { QueryClient, QueryClientProvider } from 'react-query'

        export function renderHookWithProviders(
          hook,
          {
            queryClient = new QueryClient(),
            ...options
          } = {}
        ) {
          const wrapper = ({ children }) => (
            <QueryClientProvider client={queryClient}>
              {children}
            </QueryClientProvider>
          )
          
          return renderHook(hook, { wrapper, ...options })
        }

        export function createQueryClient() {
          return new QueryClient({
            defaultOptions: {
              queries: {
                retry: false,
                cacheTime: 0
              }
            }
          })
        }

        export function waitForNextUpdate(result, timeout = 1000) {
          return new Promise((resolve, reject) => {
            const timer = setTimeout(() => {
              reject(new Error('Timed out waiting for update'))
            }, timeout)
            
            result.waitForNextUpdate().then(() => {
              clearTimeout(timer)
              resolve()
            })
          })
        }

        // 使用示例
        describe('useUser', () => {
          it('should fetch user data', async () => {
            const queryClient = createQueryClient()
            
            const { result } = renderHookWithProviders(
              () => useUser(1),
              { queryClient }
            )
            
            expect(result.current.isLoading).toBe(true)
            await waitForNextUpdate(result)
            
            expect(result.current.data).toEqual({
              id: 1,
              name: 'John'
            })
          })
        })
        """, language="javascript")

# 添加部署配置
st.header("部署配置")

deploy_col1, deploy_col2 = st.columns(2)

with deploy_col1:
    with st.expander("Docker配置", expanded=True):
        st.code("""
        # Dockerfile
        # 构建阶段
        FROM node:18-alpine AS builder
        WORKDIR /app
        COPY package*.json ./
        RUN npm ci
        COPY . .
        RUN npm run build

        # 生产阶段
        FROM node:18-alpine AS runner
        WORKDIR /app

        ENV NODE_ENV production

        # 添加非root用户
        RUN addgroup --system --gid 1001 nodejs
        RUN adduser --system --uid 1001 nextjs

        COPY --from=builder /app/next.config.js ./
        COPY --from=builder /app/public ./public
        COPY --from=builder /app/.next/standalone ./
        COPY --from=builder /app/.next/static ./.next/static

        USER nextjs

        EXPOSE 3000

        ENV PORT 3000
        ENV HOSTNAME "0.0.0.0"

        CMD ["node", "server.js"]

        # docker-compose.yml
        version: '3.8'

        services:
          web:
            build: .
            ports:
              - "3000:3000"
            environment:
              - DATABASE_URL=postgres://user:pass@db:5432/dbname
              - REDIS_URL=redis://cache:6379
            depends_on:
              - db
              - cache

          db:
            image: postgres:14-alpine
            volumes:
              - postgres_data:/var/lib/postgresql/data
            environment:
              - POSTGRES_USER=user
              - POSTGRES_PASSWORD=pass
              - POSTGRES_DB=dbname

          cache:
            image: redis:alpine
            volumes:
              - redis_data:/data

        volumes:
          postgres_data:
          redis_data:
        """, language="dockerfile")

with deploy_col2:
    with st.expander("部署脚本", expanded=True):
        st.code("""
        // scripts/deploy.js
        const { exec } = require('child_process')
        const { promisify } = require('util')
        const execAsync = promisify(exec)

        async function deploy() {
          try {
            // 运行测试
            console.log('Running tests...')
            await execAsync('npm test')

            // 构建应用
            console.log('Building application...')
            await execAsync('npm run build')

            // 运行数据库迁移
            console.log('Running database migrations...')
            await execAsync('npm run migrate')

            // 部署到生产环境
            console.log('Deploying to production...')
            await execAsync('docker-compose up -d --build')

            console.log('Deployment successful!')
          } catch (error) {
            console.error('Deployment failed:', error)
            process.exit(1)
          }
        }

        // 部署配置
        module.exports = {
          apps: [{
            name: 'next-app',
            script: 'npm',
            args: 'start',
            instances: 'max',
            exec_mode: 'cluster',
            autorestart: true,
            watch: false,
            max_memory_restart: '1G',
            env: {
              NODE_ENV: 'production'
            }
          }]
        }
        """, language="javascript")

# 添加日志系统
st.header("日志系统")

log_col1, log_col2 = st.columns(2)

with log_col1:
    with st.expander("日志配置", expanded=True):
        st.code("""
        // lib/logger.js
        import pino from 'pino'

        const config = {
          development: {
            transport: {
              target: 'pino-pretty',
              options: {
                colorize: true
              }
            },
            level: 'debug'
          },
          production: {
            transport: {
              target: 'pino/file',
              options: { destination: '/var/log/app.log' }
            },
            level: 'info'
          }
        }

        class Logger {
          constructor() {
            this.logger = pino(config[process.env.NODE_ENV || 'development'])
            this.context = {}
          }

          setContext(context) {
            this.context = { ...this.context, ...context }
          }

          log(level, message, meta = {}) {
            this.logger[level]({
              ...this.context,
              ...meta,
              timestamp: new Date().toISOString()
            }, message)
          }

          info(message, meta) {
            this.log('info', message, meta)
          }

          error(message, meta) {
            this.log('error', message, meta)
          }

          warn(message, meta) {
            this.log('warn', message, meta)
          }

          debug(message, meta) {
            this.log('debug', message, meta)
          }
        }

        export const logger = new Logger()
        """, language="javascript")

with log_col2:
    with st.expander("日志中间件", expanded=True):
        st.code("""
        // middleware/logger.js
        import { logger } from '../lib/logger'

        export function loggerMiddleware(req, res, next) {
          const start = Date.now()
          
          // 请求日志
          logger.info('Incoming request', {
            method: req.method,
            url: req.url,
            headers: req.headers,
            query: req.query,
            body: req.body
          })

          // 响应拦截
          const originalEnd = res.end
          res.end = function(...args) {
            const duration = Date.now() - start
            
            logger.info('Outgoing response', {
              statusCode: res.statusCode,
              duration,
              headers: res.getHeaders()
            })
            
            originalEnd.apply(res, args)
          }

          next()
        }

        // 错误日志中间件
        export function errorLoggerMiddleware(err, req, res, next) {
          logger.error('Unhandled error', {
            error: {
              message: err.message,
              stack: err.stack,
              name: err.name
            },
            request: {
              method: req.method,
              url: req.url,
              headers: req.headers,
              query: req.query,
              body: req.body
            }
          })

          next(err)
        }

        // 使用示例
        import { createLogger, format, transports } from 'winston'

        const logger = createLogger({
          level: 'info',
          format: format.combine(
            format.timestamp(),
            format.json()
          ),
          transports: [
            new transports.File({ 
              filename: 'error.log', 
              level: 'error' 
            }),
            new transports.File({ 
              filename: 'combined.log' 
            })
          ]
        })

        if (process.env.NODE_ENV !== 'production') {
          logger.add(new transports.Console({
            format: format.simple()
          }))
        }

        export { logger }
        """, language="javascript")

