import streamlit as st

st.title("SwiftUI Cheatsheet")

# 顶部参考资源
with st.expander("参考资源", expanded=True):
    st.markdown("""
    - [苹果官方SwiftUI教程](https://developer.apple.com/cn/documentation/swiftui/)
    - [SwiftUI Apple Developer](https://developer.apple.com/xcode/swiftui/)
    - [Hacking With Swift](https://www.hackingwithswift.com/quick-start/swiftui)
    - [SwiftUI Lab](https://swiftui-lab.com)
    """)

# 选项卡
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15 = st.tabs([
    "基础组件", "导航和布局", "状态和动画", 
    "高级特性", "测试和调试", "特殊主题", 
    "平台特性", "跨平台开发", "系统集成",
    "系统功能", "高级功能", "高级功能2", "网络安全",
    "系统扩展", "系统功能2"
])

# Tab 1 - 基础组件
with tab1:
    left_col, right_col = st.columns(2)
    
    # 左栏继续保持基础组件
    with left_col:
        st.header("基础组件")
        
        # Text 组件
        with st.expander("Text", expanded=True):
            st.code("""
            // 基础文本
            Text("Hello World")
                .font(.title)
                .foregroundColor(.blue)
                .padding()
                
            // 富文本
            Text("Hello")
                + Text(" World").bold()
                
            // 多行文本
            Text(\"\"\"
            First Line
            Second Line
            Third Line
            \"\"\")
            """, language="swift")
        
        # Button 组件
        with st.expander("Button", expanded=True):
            st.code("""
            // 基础按钮
            Button("Click Me") {
                print("Button tapped!")
            }
            
            // 自定义按钮
            Button(action: {
                // 处理点击
            }) {
                HStack {
                    Image(systemName: "star.fill")
                    Text("Favorite")
                }
                .padding()
                .background(Color.blue)
                .foregroundColor(.white)
                .cornerRadius(10)
            }
            """, language="swift")
        
        # TextField 组件
        with st.expander("TextField", expanded=True):
            st.code("""
            @State private var text = ""
            
            TextField("Enter text", text: $text)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                
            SecureField("Password", text: $password)
                .textFieldStyle(RoundedBorderTextFieldStyle())
            """, language="swift")
        
        # Toggle 组件
        with st.expander("Toggle", expanded=True):
            st.code("""
            @State private var isOn = false
            
            Toggle("Notifications", isOn: $isOn)
            
            // 自定义样式
            Toggle(isOn: $isOn) {
                HStack {
                    Image(systemName: "bell.fill")
                    Text("Alerts")
                }
            }
            .toggleStyle(SwitchToggleStyle(tint: .blue))
            """, language="swift")
        
        # Picker 组件
        with st.expander("Picker", expanded=True):
            st.code("""
            @State private var selection = 1
            
            Picker("Choose", selection: $selection) {
                Text("Option 1").tag(1)
                Text("Option 2").tag(2)
                Text("Option 3").tag(3)
            }
            
            // 分段控制器样式
            Picker("Options", selection: $selection) {
                Text("One").tag(1)
                Text("Two").tag(2)
            }
            .pickerStyle(SegmentedPickerStyle())
            """, language="swift")
    
    # 右栏添加更多控件
    with right_col:
        st.header("交互控件")
        
        # Slider
        with st.expander("Slider", expanded=True):
            st.code("""
            @State private var value = 50.0
            
            Slider(value: $value, in: 0...100) {
                Text("Speed")
            } minimumValueLabel: {
                Text("0")
            } maximumValueLabel: {
                Text("100")
            }
            """, language="swift")
        
        # Stepper
        with st.expander("Stepper", expanded=True):
            st.code("""
            @State private var quantity = 1
            
            Stepper("Quantity: \(quantity)", value: $quantity, in: 1...10)
            
            // 自定义步进
            Stepper("Value: \(value)") {
                value += 5
            } onDecrement: {
                value -= 5
            }
            """, language="swift")
        
        # DatePicker
        with st.expander("DatePicker", expanded=True):
            st.code("""
            @State private var date = Date()
            
            DatePicker(
                "Start Date",
                selection: $date,
                displayedComponents: [.date, .hourAndMinute]
            )
            
            // 紧凑样式
            DatePicker("", selection: $date)
                .datePickerStyle(CompactDatePickerStyle())
                .labelsHidden()
            """, language="swift")

# Tab 2 - 导航和布局
with tab2:
    left_col, right_col = st.columns(2)
    
    # 左栏 - 导航组件
    with left_col:
        st.header("导航组件")
        
        # NavigationView
        with st.expander("NavigationView", expanded=True):
            st.code("""
            NavigationView {
                List {
                    NavigationLink("Detail 1") {
                        Text("Detail View 1")
                    }
                    NavigationLink("Detail 2") {
                        Text("Detail View 2")
                    }
                }
                .navigationTitle("Home")
                .navigationBarItems(
                    trailing: Button("Add") {
                        // Action
                    }
                )
            }
            """, language="swift")
        
        # TabView
        with st.expander("TabView", expanded=True):
            st.code("""
            TabView {
                Text("Tab 1")
                    .tabItem {
                        Image(systemName: "1.circle")
                        Text("First")
                    }
                
                Text("Tab 2")
                    .tabItem {
                        Image(systemName: "2.circle")
                        Text("Second")
                    }
            }
            """, language="swift")
    
    # 右栏 - 弹出视图
    with right_col:
        st.header("弹出视图")
        
        # Alert
        with st.expander("Alert", expanded=True):
            st.code("""
            @State private var showingAlert = false
            
            Button("Show Alert") {
                showingAlert = true
            }
            .alert("Important Message", isPresented: $showingAlert) {
                Button("OK", role: .cancel) { }
            } message: {
                Text("This is an alert message")
            }
            """, language="swift")
        
        # Sheet
        with st.expander("Sheet", expanded=True):
            st.code("""
            @State private var showingSheet = false
            
            Button("Show Sheet") {
                showingSheet = true
            }
            .sheet(isPresented: $showingSheet) {
                SheetView()
            }
            
            struct SheetView: View {
                @Environment(\\.dismiss) var dismiss
                
                var body: some View {
                    Button("Dismiss") {
                        dismiss()
                    }
                }
            }
            """, language="swift")
        
        # ActionSheet
        with st.expander("ActionSheet", expanded=True):
            st.code("""
            @State private var showingActionSheet = false
            
            Button("Show Action Sheet") {
                showingActionSheet = true
            }
            .confirmationDialog("Select Option", isPresented: $showingActionSheet) {
                Button("Option 1") { }
                Button("Option 2") { }
                Button("Cancel", role: .cancel) { }
            }
            """, language="swift")

# Tab 3 - 状态和动画
with tab3:
    left_col, right_col = st.columns(2)
    
    # 左栏 - 状态管理
    with left_col:
        st.header("状态管理")
        
        # @State
        with st.expander("@State", expanded=True):
            st.code("""
            struct CounterView: View {
                @State private var count = 0
                
                var body: some View {
                    VStack {
                        Text("Count: \(count)")
                        Button("Increment") {
                            count += 1
                        }
                    }
                }
            }
            """, language="swift")
        
        # @Binding
        with st.expander("@Binding", expanded=True):
            st.code("""
            struct ToggleView: View {
                @Binding var isOn: Bool
                
                var body: some View {
                    Toggle("Switch", isOn: $isOn)
                }
            }
            
            struct ParentView: View {
                @State private var isOn = false
                
                var body: some View {
                    ToggleView(isOn: $isOn)
                }
            }
            """, language="swift")
        
        # @ObservedObject
        with st.expander("@ObservedObject", expanded=True):
            st.code("""
            class UserViewModel: ObservableObject {
                @Published var username = ""
                @Published var isLoggedIn = false
                
                func login() {
                    // 登录逻辑
                    isLoggedIn = true
                }
            }
            
            struct UserView: View {
                @ObservedObject var viewModel: UserViewModel
                
                var body: some View {
                    VStack {
                        TextField("Username", text: $viewModel.username)
                        Button("Login") {
                            viewModel.login()
                        }
                    }
                }
            }
            """, language="swift")
    
    # 右栏 - 动画
    with right_col:
        st.header("动画效果")
        
        # 基础动画
        with st.expander("基础动画", expanded=True):
            st.code("""
            @State private var isAnimated = false
            
            // 隐式动画
            Circle()
                .frame(width: isAnimated ? 100 : 50)
                .animation(.spring(), value: isAnimated)
            
            // 显式动画
            Button("Animate") {
                withAnimation(.easeInOut(duration: 1)) {
                    isAnimated.toggle()
                }
            }
            """, language="swift")
        
        # 转场动画
        with st.expander("转场动画", expanded=True):
            st.code("""
            @State private var showView = false
            
            VStack {
                if showView {
                    Text("Animated View")
                        .transition(.scale.combined(with: .opacity))
                }
                
                Button("Toggle") {
                    withAnimation {
                        showView.toggle()
                    }
                }
            }
            """, language="swift")
        
        # 自定义动画
        with st.expander("自定义动画", expanded=True):
            st.code("""
            // 自定义动画修饰符
            struct Shake: GeometryEffect {
                var amount: CGFloat = 10
                var shakesPerUnit = 3
                var animatableData: CGFloat
                
                func effectValue(size: CGSize) -> ProjectionTransform {
                    ProjectionTransform(
                        CGAffineTransform(translationX:
                            amount * sin(animatableData * .pi * CGFloat(shakesPerUnit)),
                            y: 0)
                    )
                }
            }
            
            // 使用自定义动画
            @State private var shake = false
            
            Text("Shake me!")
                .modifier(Shake(animatableData: shake ? 1 : 0))
                .onTapGesture {
                    withAnimation(.default) {
                        shake.toggle()
                    }
                }
            """, language="swift")

# Tab 4 - 高级特性
with tab4:
    left_col, right_col = st.columns(2)
    
    # 左栏 - 自定义修饰符
    with left_col:
        st.header("自定义修饰符")
        
        # ViewModifier
        with st.expander("ViewModifier", expanded=True):
            st.code("""
            // 自定义修饰符
            struct CardStyle: ViewModifier {
                func body(content: Content) -> some View {
                    content
                        .padding()
                        .background(Color.white)
                        .cornerRadius(10)
                        .shadow(radius: 5)
                }
            }
            
            // 扩展View
            extension View {
                func cardStyle() -> some View {
                    modifier(CardStyle())
                }
            }
            
            // 使用自定义修饰符
            Text("Card Style")
                .cardStyle()
            """, language="swift")
        
        # 环境值
        with st.expander("环境值", expanded=True):
            st.code("""
            // 自定义环境键
            private struct ThemeKey: EnvironmentKey {
                static let defaultValue = Theme.light
            }
            
            extension EnvironmentValues {
                var theme: Theme {
                    get { self[ThemeKey.self] }
                    set { self[ThemeKey.self] = newValue }
                }
            }
            
            // 使用环境值
            struct ThemedView: View {
                @Environment(\\.theme) var theme
                
                var body: some View {
                    Text("Themed")
                        .foregroundColor(theme.textColor)
                }
            }
            """, language="swift")
        
        # PreferenceKey
        with st.expander("PreferenceKey", expanded=True):
            st.code("""
            // 自定义PreferenceKey
            struct HeightPreferenceKey: PreferenceKey {
                static var defaultValue: CGFloat = 0
                
                static func reduce(value: inout CGFloat,
                                nextValue: () -> CGFloat) {
                    value = max(value, nextValue())
                }
            }
            
            // 使用PreferenceKey
            struct MeasuredView: View {
                var body: some View {
                    Text("Measure me")
                        .background(GeometryReader { proxy in
                            Color.clear.preference(
                                key: HeightPreferenceKey.self,
                                value: proxy.size.height
                            )
                        })
                }
            }
            """, language="swift")
    
    # 右栏 - 性能优化
    with right_col:
        st.header("性能优化")
        
        # 布局优化
        with st.expander("布局优化", expanded=True):
            st.code("""
            // 使用LazyStack
            LazyVStack {
                ForEach(0..<1000) { i in
                    Text("Row \(i)")
                }
            }
            
            // 使用ID标识
            ForEach(items, id: \\.id) { item in
                ItemView(item: item)
                    .id(item.id)  // 优化重新渲染
            }
            
            // 避免嵌套视图
            struct OptimizedView: View {
                @State private var data = [Item]()
                
                var body: some View {
                    ScrollView {
                        LazyVStack {
                            ForEach(data) { item in
                                ItemRow(item: item)
                            }
                        }
                    }
                }
            }
            """, language="swift")
        
        # 内存管理
        with st.expander("内存管理", expanded=True):
            st.code("""
            // 使用Equatable
            struct ContentView: View, Equatable {
                let title: String
                
                static func == (lhs: ContentView, rhs: ContentView) -> Bool {
                    lhs.title == rhs.title
                }
            }
            
            // 避免闭包捕获
            class ViewModel: ObservableObject {
                @Published var data: [Item] = []
                
                func loadData() {
                    // 使用 [weak self]
                    Task { [weak self] in
                        let items = await fetchItems()
                        self?.data = items
                    }
                }
            }
            """, language="swift")
        
        # 异步加载
        with st.expander("异步加载", expanded=True):
            st.code("""
            // 异步图片加载
            AsyncImage(url: URL(string: "https://example.com/image.jpg")) { phase in
                switch phase {
                case .empty:
                    ProgressView()
                case .success(let image):
                    image.resizable()
                case .failure:
                    Image(systemName: "photo")
                @unknown default:
                    EmptyView()
                }
            }
            
            // 任务管理
            struct DataView: View {
                @State private var data: [Item] = []
                
                var body: some View {
                    List(data) { item in
                        Text(item.title)
                    }
                    .task {
                        await loadData()
                    }
                }
                
                func loadData() async {
                    data = await fetchItems()
                }
            }
            """, language="swift")

    # 添加最佳实践部分
    st.header("最佳实践")

    best_col1, best_col2 = st.columns(2)

    with best_col1:
        with st.expander("架构模式", expanded=True):
            st.code("""
            // MVVM架构
            class HomeViewModel: ObservableObject {
                @Published var items: [Item] = []
                @Published var isLoading = false
                @Published var error: Error?
                
                func fetchItems() async {
                    isLoading = true
                    do {
                        items = try await apiClient.fetchItems()
                    } catch {
                        self.error = error
                    }
                    isLoading = false
                }
            }
            
            struct HomeView: View {
                @StateObject var viewModel = HomeViewModel()
                
                var body: some View {
                    Group {
                        if viewModel.isLoading {
                            ProgressView()
                        } else if let error = viewModel.error {
                            ErrorView(error: error)
                        } else {
                            ItemsList(items: viewModel.items)
                        }
                    }
                    .task {
                        await viewModel.fetchItems()
                    }
                }
            }
            """, language="swift")

    with best_col2:
        with st.expander("代码组织", expanded=True):
            st.code("""
            // 视图组件化
            struct ItemRow: View {
                let item: Item
                
                var body: some View {
                    VStack(alignment: .leading) {
                        Text(item.title)
                            .font(.headline)
                        Text(item.description)
                            .font(.subheadline)
                    }
                }
            }
            
            // 扩展功能分离
            extension View {
                func errorAlert(error: Binding<Error?>) -> some View {
                    alert(
                        "Error",
                        isPresented: .constant(error.wrappedValue != nil),
                        actions: {
                            Button("OK") {
                                error.wrappedValue = nil
                            }
                        },
                        message: {
                            Text(error.wrappedValue?.localizedDescription ?? "")
                        }
                    )
                }
            }
            """, language="swift")

    # 添加手势识别部分
    st.header("手势识别")

    gesture_col1, gesture_col2 = st.columns(2)

    with gesture_col1:
        # 基础手势
        with st.expander("基础手势", expanded=True):
            st.code("""
            // 点击手势
            Text("Tap me")
                .onTapGesture {
                    print("Tapped!")
                }
            
            // 长按手势
            Text("Long press me")
                .onLongPressGesture(minimumDuration: 1) {
                    print("Long pressed!")
                }
            """, language="swift")
        
        # 拖动手势
        with st.expander("拖动手势", expanded=True):
            st.code("""
            @State private var offset = CGSize.zero
            
            Text("Drag me")
                .offset(offset)
                .gesture(
                    DragGesture()
                        .onChanged { value in
                            offset = value.translation
                        }
                        .onEnded { _ in
                            withAnimation {
                                offset = .zero
                            }
                        }
                )
            """, language="swift")

    with gesture_col2:
        # 复杂手势
        with st.expander("复杂手势", expanded=True):
            st.code("""
            // 组合手势
            let drag = DragGesture()
            let tap = TapGesture()
            
            Text("Complex gesture")
                .gesture(
                    SequenceGesture(tap, drag)
                )
            
            // 缩放手势
            @State private var scale: CGFloat = 1.0
            
            Image("photo")
                .scaleEffect(scale)
                .gesture(
                    MagnificationGesture()
                        .onChanged { value in
                            scale = value
                        }
                )
            """, language="swift")
        
        # 自定义手势
        with st.expander("自定义手势", expanded=True):
            st.code("""
            struct CustomGesture: Gesture {
                var minimumDistance: CGFloat = 30
                
                var body: some Gesture {
                    DragGesture()
                        .onEnded { value in
                            if abs(value.translation.width) > minimumDistance {
                                // 处理手势
                            }
                        }
                }
            }
            
            // 使用自定义手势
            Text("Custom gesture")
                .gesture(CustomGesture())
            """, language="swift")



# Tab 5 - 测试和调试
with tab5:
    left_col, right_col = st.columns(2)
    
    # 左栏 - 测试
    with left_col:
        st.header("单元测试")
        
        # 视图测试
        with st.expander("视图测试", expanded=True):
            st.code("""
            import XCTest
            @testable import YourApp

            class ContentViewTests: XCTestCase {
                func testContentViewTitle() {
                    // 创建视图
                    let view = ContentView()
                    
                    // 获取标题文本
                    let title = view.title
                    
                    // 验证标题
                    XCTAssertEqual(title, "Expected Title")
                }
                
                func testButtonTap() {
                    // 创建ViewModel
                    let viewModel = ContentViewModel()
                    
                    // 模拟按钮点击
                    viewModel.buttonTapped()
                    
                    // 验证结果
                    XCTAssertTrue(viewModel.isButtonTapped)
                }
            }
            """, language="swift")
        
        # 预览测试
        with st.expander("预览测试", expanded=True):
            st.code("""
            struct ContentView_Previews: PreviewProvider {
                static var previews: some View {
                    Group {
                        // 默认状态
                        ContentView()
                        
                        // 加载状态
                        ContentView()
                            .previewDisplayName("Loading")
                            .onAppear {
                                viewModel.isLoading = true
                            }
                        
                        // 错误状态
                        ContentView()
                            .previewDisplayName("Error")
                            .onAppear {
                                viewModel.error = SampleError()
                            }
                        
                        // 深色模式
                        ContentView()
                            .preferredColorScheme(.dark)
                    }
                }
            }
            """, language="swift")
    
    # 右栏 - 调试
    with right_col:
        st.header("调试技巧")
        
        # 调试工具
        with st.expander("调试工具", expanded=True):
            st.code("""
            // 打印调试
            Text("Debug")
                .onAppear {
                    print("View appeared")
                }
                .onChange(of: someValue) { newValue in
                    print("Value changed to: \\(newValue)")
                }
            
            // 时间性能
            let start = CFAbsoluteTimeGetCurrent()
            // 执行代码
            let diff = CFAbsoluteTimeGetCurrent() - start
            print("Took \\(diff) seconds")
            
            // 内存测试
            class ViewModel {
                deinit {
                    print("ViewModel deallocated")
                }
            }
            """, language="swift")
        
        # SwiftUI检查器
        with st.expander("SwiftUI检查器", expanded=True):
            st.code("""
            Text("Inspect me")
                .border(Color.red) // 显示边界
                .overlay(GeometryReader { proxy in
                    Color.clear.onAppear {
                        print("Size: \\(proxy.size)")
                    }
                })
            
            // 调试修饰符
            .debugModifier()
            
            // 自定义调试修饰符
            extension View {
                func debugModifier() -> some View {
                    self.modifier(DebugModifier())
                }
            }
            
            struct DebugModifier: ViewModifier {
                func body(content: Content) -> some View {
                    content
                        .border(Color.red)
                        .overlay(
                            Text("Debug")
                                .foregroundColor(.red)
                        )
                }
            }
            """, language="swift")

    # 添加UIKit集成部分
    st.header("UIKit 集成")

    uikit_col1, uikit_col2 = st.columns(2)

    with uikit_col1:
        with st.expander("UIKit视图封装", expanded=True):
            st.code("""
            // 封装UIKit视图
            struct UIKitView: UIViewRepresentable {
                func makeUIView(context: Context) -> UIView {
                    // 创建UIKit视图
                    let view = UIView()
                    view.backgroundColor = .red
                    return view
                }
                
                func updateUIView(_ uiView: UIView, context: Context) {
                    // 更新视图
                }
            }
            
            // 封装UIViewController
            struct UIKitViewController: UIViewControllerRepresentable {
                func makeUIViewController(context: Context) -> UIViewController {
                    // 创建UIViewController
                    let viewController = UIViewController()
                    return viewController
                }
                
                func updateUIViewController(_ uiViewController: UIViewController,
                                        context: Context) {
                    // 更新视图控制器
                }
            }
            """, language="swift")

    with uikit_col2:
        with st.expander("SwiftUI与UIKit交互", expanded=True):
            st.code("""
            // 在UIKit中使用SwiftUI
            let swiftUIView = UIHostingController(rootView: ContentView())
            
            // 协调器模式
            class Coordinator: NSObject, UINavigationControllerDelegate {
                var parent: UIKitViewController
                
                init(_ parent: UIKitViewController) {
                    self.parent = parent
                }
                
                // 实现委托方法
            }
            
            // 在SwiftUI中使用UIKit手势
            struct UIKitGestureView: UIViewRepresentable {
                let onTap: () -> Void
                
                func makeUIView(context: Context) -> UIView {
                    let view = UIView()
                    let gesture = UITapGestureRecognizer(
                        target: context.coordinator,
                        action: #selector(Coordinator.handleTap)
                    )
                    view.addGestureRecognizer(gesture)
                    return view
                }
                
                func makeCoordinator() -> Coordinator {
                    Coordinator(self)
                }
                
                class Coordinator: NSObject {
                    let parent: UIKitGestureView
                    
                    init(_ parent: UIKitGestureView) {
                        self.parent = parent
                    }
                    
                    @objc func handleTap() {
                        parent.onTap()
                    }
                }
            }
            """, language="swift")

    # 添加常见问题解决方案
    st.header("常见问题解决方案")

    faq_col1, faq_col2 = st.columns(2)

    with faq_col1:
        with st.expander("性能问题", expanded=True):
            st.markdown("""
            1. 视图重绘过多
            - 使用 `@State` 而不是 `@ObservedObject`
            - 避免不必要的视图更新
            - 使用 `equatable` 优化

            2. 内存泄漏
            - 正确使用 `weak self`
            - 注意循环引用
            - 检查 deinit 调用

            3. 列表性能
            - 使用 `LazyVStack`
            - 实现 `Identifiable`
            - 避免嵌套 ForEach
            """)

    with faq_col2:
        with st.expander("布局问题", expanded=True):
            st.markdown("""
            1. 布局约束冲突
            - 检查frame设���
            - 使用GeometryReader
            - 避免硬编码尺寸

            2. 动态高度
            - 使用ScrollView
            - 实现动态计算
            - 注意布局优先级

            3. 键盘处理
            - 使用.ignoresSafeArea(.keyboard)
            - 实现键盘监听
            - 添加滚动视图
            """)

# Tab 6 - 特殊主题
with tab6:
    left_col, right_col = st.columns(2)
    
    # 左栏 - 图表和可视化
    with left_col:
        st.header("图表和可视化")
        
        # 基础图表
        with st.expander("基础图表", expanded=True):
            st.code("""
            // 柱状图
            struct BarChart: View {
                let data: [Double]
                
                var body: some View {
                    HStack(alignment: .bottom, spacing: 2) {
                        ForEach(data.indices, id: \\.self) { index in
                            Rectangle()
                                .fill(Color.blue)
                                .frame(width: 30, height: data[index])
                        }
                    }
                }
            }
            
            // 折线图
            struct LineChart: View {
                let points: [CGPoint]
                
                var body: some View {
                    Path { path in
                        guard let first = points.first else { return }
                        path.move(to: first)
                        points.dropFirst().forEach {
                            path.addLine(to: $0)
                        }
                    }
                    .stroke(Color.blue, lineWidth: 2)
                }
            }
            """, language="swift")
        
        # 自定义形状
        with st.expander("自定义形状", expanded=True):
            st.code("""
            struct CustomShape: Shape {
                func path(in rect: CGRect) -> Path {
                    var path = Path()
                    
                    path.move(to: CGPoint(x: rect.midX, y: rect.minY))
                    path.addQuadCurve(
                        to: CGPoint(x: rect.maxX, y: rect.midY),
                        control: CGPoint(x: rect.maxX, y: rect.minY)
                    )
                    path.addLine(to: CGPoint(x: rect.midX, y: rect.maxY))
                    path.addLine(to: CGPoint(x: rect.minX, y: rect.midY))
                    path.closeSubpath()
                    
                    return path
                }
            }
            """, language="swift")
    
    # 右栏 - 高级动画
    with right_col:
        st.header("高级动画")
        
        # 自定义动画
        with st.expander("自定义动画", expanded=True):
            st.code("""
            // 弹性动画
            struct BounceAnimation: View {
                @State private var bounce = false
                
                var body: some View {
                    Circle()
                        .frame(width: 50, height: 50)
                        .offset(y: bounce ? 0 : -100)
                        .animation(
                            .spring(
                                response: 0.5,
                                dampingFraction: 0.5,
                                blendDuration: 0
                            ),
                            value: bounce
                        )
                        .onTapGesture {
                            bounce.toggle()
                        }
                }
            }
            
            // 循环动画
            struct PulseAnimation: View {
                @State private var scale: CGFloat = 1
                
                var body: some View {
                    Circle()
                        .scaleEffect(scale)
                        .opacity(2 - scale)
                        .onAppear {
                            withAnimation(
                                .easeInOut(duration: 1)
                                .repeatForever(autoreverses: false)
                            ) {
                                scale = 2
                            }
                        }
                }
            }
            """, language="swift")
        
        # 手势动画
        with st.expander("手势动画", expanded=True):
            st.code("""
            struct DraggableCard: View {
                @State private var offset = CGSize.zero
                @State private var scale: CGFloat = 1
                
                var body: some View {
                    RoundedRectangle(cornerRadius: 10)
                        .fill(Color.blue)
                        .frame(width: 100, height: 150)
                        .offset(offset)
                        .scaleEffect(scale)
                        .gesture(
                            DragGesture()
                                .onChanged { gesture in
                                    offset = gesture.translation
                                    scale = 1.1
                                }
                                .onEnded { _ in
                                    withAnimation(.spring()) {
                                        offset = .zero
                                        scale = 1
                                    }
                                }
                        )
                }
            }
            """, language="swift")

    # 添加自定义控件部分
    st.header("自定义控件")

    custom_col1, custom_col2 = st.columns(2)

    with custom_col1:
        with st.expander("评分控件", expanded=True):
            st.code("""
            struct RatingView: View {
                @Binding var rating: Int
                let maxRating: Int = 5
                
                var body: some View {
                    HStack {
                        ForEach(1...maxRating, id: \\.self) { number in
                            Image(systemName: number <= rating ? 
                                "star.fill" : "star")
                                .foregroundColor(.yellow)
                                .onTapGesture {
                                    rating = number
                                }
                        }
                    }
                }
            }
            """, language="swift")
        
        with st.expander("进度指示器", expanded=True):
            st.code("""
            struct CircularProgressView: View {
                let progress: Double
                
                var body: some View {
                    Circle()
                        .trim(from: 0, to: CGFloat(progress))
                        .stroke(
                            Color.blue,
                            style: StrokeStyle(
                                lineWidth: 10,
                                lineCap: .round
                            )
                        )
                        .rotationEffect(.degrees(-90))
                        .animation(.spring(), value: progress)
                }
            }
            """, language="swift")

    with custom_col2:
        with st.expander("标签输入框", expanded=True):
            st.code("""
            struct TagInputField: View {
                @Binding var tags: [String]
                @State private var inputText = ""
                
                var body: some View {
                    VStack {
                        // 标签显示
                        FlowLayout(spacing: 8) {
                            ForEach(tags, id: \\.self) { tag in
                                TagView(text: tag) {
                                    tags.removeAll { $0 == tag }
                                }
                            }
                        }
                        
                        // 输���框
                        TextField("Add tag", text: $inputText)
                            .onSubmit {
                                if !inputText.isEmpty {
                                    tags.append(inputText)
                                    inputText = ""
                                }
                            }
                    }
                }
            }
            
            struct TagView: View {
                let text: String
                let onDelete: () -> Void
                
                var body: some View {
                    HStack {
                        Text(text)
                        Button(action: onDelete) {
                            Image(systemName: "xmark.circle.fill")
                        }
                    }
                    .padding(.horizontal, 8)
                    .padding(.vertical, 4)
                    .background(Color.blue.opacity(0.2))
                    .cornerRadius(8)
                }
            }
            """, language="swift")

# Tab 7 - 平台特性
with tab7:
    left_col, right_col = st.columns(2)
    
    # 左栏 - 辅助功能
    with left_col:
        st.header("辅助功能")
        
        # 基础辅助功能
        with st.expander("基础辅助功能", expanded=True):
            st.code("""
            Text("Accessible Text")
                .accessibilityLabel("This is a label")
                .accessibilityHint("This is a hint")
                
            Button(action: {}) {
                Text("Action")
            }
            .accessibilityAddTraits(.isButton)
            .accessibilityValue("Button Value")
            
            // 自定义朗读
            Image("photo")
                .accessibilityLabel("Profile photo")
                .accessibilityRemoveTraits(.isImage)
            """, language="swift")
        
        # 动态字体
        with st.expander("动态字体", expanded=True):
            st.code("""
            // 支持动态字体大小
            Text("Dynamic Text")
                .font(.body)
                .dynamicTypeSize(...DynamicTypeSize.xxxLarge)
            
            // 自定义缩放
            struct ScalableText: View {
                @Environment(\\.dynamicTypeSize) var dynamicTypeSize
                
                var body: some View {
                    Text("Scalable")
                        .font(.system(size: baseSize * dynamicScale))
                }
                
                var dynamicScale: CGFloat {
                    switch dynamicTypeSize {
                    case .xSmall: return 0.8
                    case .small: return 0.9
                    case .medium: return 1.0
                    case .large: return 1.1
                    case .xLarge: return 1.2
                    default: return 1.3
                    }
                }
            }
            """, language="swift")
    
    # 右栏 - Widget开发
    with right_col:
        st.header("Widget开发")
        
        # Widget基础
        with st.expander("Widget基础", expanded=True):
            st.code("""
            struct MyWidget: Widget {
                private let kind: String = "MyWidget"
                
                var body: some WidgetConfiguration {
                    StaticConfiguration(
                        kind: kind,
                        provider: MyTimelineProvider()
                    ) { entry in
                        MyWidgetEntryView(entry: entry)
                    }
                    .configurationDisplayName("My Widget")
                    .description("Widget description")
                    .supportedFamilies([.systemSmall, .systemMedium])
                }
            }
            
            struct MyWidgetEntryView: View {
                let entry: MyTimelineEntry
                
                var body: some View {
                    VStack {
                        Text(entry.date, style: .time)
                        Text(entry.data)
                    }
                }
            }
            """, language="swift")
        
        # Timeline Provider
        with st.expander("Timeline Provider", expanded=True):
            st.code("""
            struct MyTimelineProvider: TimelineProvider {
                func placeholder(in context: Context) -> MyTimelineEntry {
                    MyTimelineEntry(date: Date(), data: "Placeholder")
                }
                
                func getSnapshot(in context: Context, 
                               completion: @escaping (MyTimelineEntry) -> Void) {
                    let entry = MyTimelineEntry(
                        date: Date(),
                        data: "Snapshot"
                    )
                    completion(entry)
                }
                
                func getTimeline(in context: Context,
                               completion: @escaping (Timeline<MyTimelineEntry>) -> Void) {
                    var entries: [MyTimelineEntry] = []
                    let currentDate = Date()
                    
                    for hourOffset in 0..<5 {
                        let entryDate = Calendar.current.date(
                            byAdding: .hour,
                            value: hourOffset,
                            to: currentDate
                        )!
                        entries.append(
                            MyTimelineEntry(
                                date: entryDate,
                                data: "Data \(hourOffset)"
                            )
                        )
                    }
                    
                    let timeline = Timeline(
                        entries: entries,
                        policy: .atEnd
                    )
                    completion(timeline)
                }
            }
            """, language="swift")

    # 添加本地化部分
    st.header("本地化")

    local_col1, local_col2 = st.columns(2)

    with local_col1:
        with st.expander("文本本地化", expanded=True):
            st.code("""
            // Localizable.strings
            "greeting" = "Hello";
            "welcome_message" = "Welcome, %@";
            
            // 使用本地化字符串
            Text("greeting".localized)
            
            Text(String(
                format: "welcome_message".localized,
                username
            ))
            
            // 扩展String
            extension String {
                var localized: String {
                    NSLocalizedString(self, comment: "")
                }
                
                func localized(with arguments: CVarArg...) -> String {
                    String(format: localized, arguments)
                }
            }
            """, language="swift")

    with local_col2:
        with st.expander("资源本地化", expanded=True):
            st.code("""
            // 图片本地化
            Image("localizedImage")
                .resizable()
                .scaledToFit()
            
            // 数字和日期格式化
            struct LocalizedView: View {
                let number: Double = 1234.56
                let date = Date()
                
                var body: some View {
                    VStack {
                        Text(number, format: .currency(code: "USD"))
                        Text(date, style: .date)
                            .environment(
                                \\.locale,
                                Locale(identifier: "zh_CN")
                            )
                    }
                }
            }
            """, language="swift")

    # 添加深��模式
    st.header("深色模式适配")

    dark_col1, dark_col2 = st.columns(2)

    with dark_col1:
        with st.expander("颜色适配", expanded=True):
            st.code("""
            // 自定义颜色
            struct CustomColors {
                static let background = Color("Background")
                static let text = Color("TextColor")
            }
            
            // 使用系统色
            Text("System Colors")
                .foregroundColor(.primary)
                .background(Color(.systemBackground))
            
            // 条件颜色
            @Environment(\\.colorScheme) var colorScheme
            
            var backgroundColor: Color {
                colorScheme == .dark ? .black : .white
            }
            """, language="swift")

    with dark_col2:
        with st.expander("资源适配", expanded=True):
            st.code("""
            // 图片适配
            Image("logo")
                .resizable()
                .preferredColorScheme(.dark)
            
            // 自定义视图适配
            struct AdaptiveView: View {
                @Environment(\\.colorScheme) var colorScheme
                
                var body: some View {
                    ZStack {
                        backgroundColor
                        content
                    }
                }
                
                var backgroundColor: Color {
                    switch colorScheme {
                    case .dark:
                        return Color.black.opacity(0.9)
                    case .light:
                        return Color.white.opacity(0.9)
                    @unknown default:
                        return Color.white.opacity(0.9)
                    }
                }
            }
            """, language="swift")

# Tab 8 - 跨平台开发
with tab8:
    left_col, right_col = st.columns(2)
    
    # 左栏 - WatchOS开发
    with left_col:
        st.header("WatchOS开发")
        
        # Watch基础组件
        with st.expander("Watch基础组件", expanded=True):
            st.code("""
            // 数字表冠输入
            struct DigitalCrownView: View {
                @State private var value = 0.0
                
                var body: some View {
                    Text("Value: \\(value, specifier: "%.1f")")
                        .focusable(true)
                        .digitalCrownRotation(
                            $value,
                            from: 0,
                            through: 100,
                            by: 1.0,
                            sensitivity: .medium
                        )
                }
            }
            
            // 合并通知
            WKNotificationScene(controller: NotificationController.self) {
                Text("Notification Content")
            }
            """, language="swift")
        
        # Watch复杂功能
        with st.expander("Watch复杂功能", expanded=True):
            st.code("""
            struct ComplicationController: CLKComplicationDataSource {
                func getCurrentTimelineEntry(
                    for complication: CLKComplication,
                    withHandler handler: @escaping (CLKComplicationTimelineEntry?) -> Void
                ) {
                    // 创建复杂功能数据
                    let template = CLKComplicationTemplateGraphicCircularView(
                        // 自定义视图
                    )
                    
                    let timelineEntry = CLKComplicationTimelineEntry(
                        date: Date(),
                        complicationTemplate: template
                    )
                    
                    handler(timelineEntry)
                }
            }
            """, language="swift")
    
    # 右栏 - MacOS特性
    with right_col:
        st.header("MacOS特性")
        
        # 菜单栏
        with st.expander("菜单栏", expanded=True):
            st.code("""
            // 自定义菜单
            struct MenuBarView: View {
                var body: some View {
                    Menu("File") {
                        Button("New") { }
                        Button("Open...") { }
                        Divider()
                        Button("Save") { }
                    }
                    
                    Menu("Edit") {
                        Button("Cut") { }
                        Button("Copy") { }
                        Button("Paste") { }
                    }
                }
            }
            
            // 上下文菜单
            Text("Right Click Me")
                .contextMenu {
                    Button("Option 1") { }
                    Button("Option 2") { }
                }
            """, language="swift")
        
        # 触控板手势
        with st.expander("触控板手势", expanded=True):
            st.code("""
            struct TrackpadGestureView: View {
                @GestureState private var magnification: CGFloat = 1.0
                @State private var scale: CGFloat = 1.0
                
                var body: some View {
                    Image("photo")
                        .scaleEffect(scale * magnification)
                        .gesture(
                            MagnificationGesture()
                                .updating($magnification) { value, state, _ in
                                    state = value
                                }
                                .onEnded { value in
                                    scale *= value
                                }
                        )
                }
            }
            """, language="swift")

    # 添加iPad多任务支持
    st.header("iPad多任务支持")

    ipad_col1, ipad_col2 = st.columns(2)

    with ipad_col1:
        with st.expander("分屏支持", expanded=True):
            st.code("""
            struct AdaptiveView: View {
                @Environment(\\.horizontalSizeClass) var horizontalSizeClass
                
                var body: some View {
                    if horizontalSizeClass == .compact {
                        // 紧凑布局
                        VStack {
                            ContentView()
                            DetailView()
                        }
                    } else {
                        // 宽屏布局
                        HStack {
                            ContentView()
                            DetailView()
                        }
                    }
                }
            }
            """, language="swift")

    with ipad_col2:
        with st.expander("拖放支持", expanded=True):
            st.code("""
            struct DragDropView: View {
                let items: [Item]
                
                var body: some View {
                    ForEach(items) { item in
                        Text(item.title)
                            .onDrag {
                                // 返回拖拽数据
                                NSItemProvider(object: item.id as NSString)
                            }
                            .onDrop(of: [.text], delegate: DropDelegate())
                    }
                }
            }
            
            struct DropDelegate: DropDelegate {
                func performDrop(info: DropInfo) -> Bool {
                    // 处理拖放
                    return true
                }
            }
            """, language="swift")

    # 添加键盘快捷键支持
    st.header("键盘快捷键")

    key_col1, key_col2 = st.columns(2)

    with key_col1:
        with st.expander("基础快捷键", expanded=True):
            st.code("""
            struct ShortcutView: View {
                var body: some View {
                    Button("Save") { }
                        .keyboardShortcut("S", modifiers: .command)
                    
                    Button("Refresh") { }
                        .keyboardShortcut("R")
                    
                    Button("Delete") { }
                        .keyboardShortcut(.delete)
                }
            }
            """, language="swift")

    with key_col2:
        with st.expander("自定义快捷键", expanded=True):
            st.code("""
            struct CustomShortcuts: View {
                var body: some View {
                    Button("Custom Action") { }
                        .keyboardShortcut("K", modifiers: [.command, .shift])
                    
                    // 组合键
                    Text("Press Cmd+Opt+Space")
                        .onKeyPress(.space, modifiers: [.command, .option]) {
                            // 处理快捷键
                            return .handled
                        }
                }
            }
            """, language="swift")

# Tab 9 - 系统集成
with tab9:
    left_col, right_col = st.columns(2)
    
    # 左栏 - 通知
    with left_col:
        st.header("通知")
        
        # 本地通知
        with st.expander("本地通知", expanded=True):
            st.code("""
            class NotificationManager {
                func requestPermission() {
                    UNUserNotificationCenter.current()
                        .requestAuthorization(
                            options: [.alert, .badge, .sound]
                        ) { granted, error in
                            if granted {
                                print("通知权限已获取")
                            }
                        }
                }
                
                func scheduleNotification() {
                    let content = UNMutableNotificationContent()
                    content.title = "提醒"
                    content.body = "这是一条本地通知"
                    content.sound = .default
                    
                    let trigger = UNTimeIntervalNotificationTrigger(
                        timeInterval: 3600,
                        repeats: false
                    )
                    
                    let request = UNNotificationRequest(
                        identifier: UUID().uuidString,
                        content: content,
                        trigger: trigger
                    )
                    
                    UNUserNotificationCenter.current()
                        .add(request)
                }
            }
            """, language="swift")
        
        # 远程通知
        with st.expander("远程通知", expanded=True):
            st.code("""
            class AppDelegate: NSObject, UIApplicationDelegate {
                func application(
                    _ application: UIApplication,
                    didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
                ) {
                    let tokenString = deviceToken.map { 
                        String(format: "%02.2hhx", $0) 
                    }.joined()
                    print("Device Token: \\(tokenString)")
                }
                
                func application(
                    _ application: UIApplication,
                    didReceiveRemoteNotification userInfo: [AnyHashable: Any],
                    fetchCompletionHandler completionHandler: 
                        @escaping (UIBackgroundFetchResult) -> Void
                ) {
                    // 处理远程通知
                    completionHandler(.newData)
                }
            }
            """, language="swift")
    
    # 右栏 - 后台任务
    with right_col:
        st.header("后台任务")
        
        # 后台刷新
        with st.expander("后台刷新", expanded=True):
            st.code("""
            class BackgroundTaskManager {
                func scheduleAppRefresh() {
                    BGAppRefreshTaskRequest(
                        identifier: "com.app.refresh"
                    ).earliestBeginDate = Date(
                        timeIntervalSinceNow: 3600
                    )
                    
                    try? BGTaskScheduler.shared.submit(
                        BGAppRefreshTaskRequest(
                            identifier: "com.app.refresh"
                        )
                    )
                }
                
                func handleAppRefresh(task: BGAppRefreshTask) {
                    // 执行后台刷新任务
                    task.expirationHandler = {
                        // 清理任务
                    }
                    
                    // 完成任���
                    task.setTaskCompleted(success: true)
                }
            }
            """, language="swift")
        
        # 后台下载
        with st.expander("后台下载", expanded=True):
            st.code("""
            class DownloadManager {
                func startBackgroundDownload(url: URL) {
                    let config = URLSessionConfiguration
                        .background(
                            withIdentifier: "com.app.download"
                        )
                    
                    let session = URLSession(
                        configuration: config,
                        delegate: self,
                        delegateQueue: nil
                    )
                    
                    let task = session.downloadTask(with: url)
                    task.resume()
                }
            }
            
            extension DownloadManager: URLSessionDownloadDelegate {
                func urlSession(
                    _ session: URLSession,
                    downloadTask: URLSessionDownloadTask,
                    didFinishDownloadingTo location: URL
                ) {
                    // 处理下载完成
                }
            }
            """, language="swift")

    # 添加数据同步
    st.header("数据同步")

    sync_col1, sync_col2 = st.columns(2)

    with sync_col1:
        with st.expander("CloudKit", expanded=True):
            st.code("""
            class CloudKitManager {
                let container = CKContainer.default()
                let database = CKContainer.default().privateCloudDatabase
                
                func saveRecord() {
                    let record = CKRecord(recordType: "Item")
                    record["name"] = "测试项目"
                    
                    database.save(record) { record, error in
                        if let error = error {
                            print("保存失败: \\(error)")
                        } else {
                            print("保存成功")
                        }
                    }
                }
                
                func fetchRecords() {
                    let query = CKQuery(
                        recordType: "Item",
                        predicate: NSPredicate(value: true)
                    )
                    
                    database.perform(query) { records, error in
                        if let error = error {
                            print("查询失败: \\(error)")
                        } else {
                            print("查询到\\(records?.count ?? 0)条记录")
                        }
                    }
                }
            }
            """, language="swift")

    with sync_col2:
        with st.expander("Core Data", expanded=True):
            st.code("""
            class CoreDataManager {
                static let shared = CoreDataManager()
                
                lazy var persistentContainer: NSPersistentContainer = {
                    let container = NSPersistentContainer(name: "Model")
                    container.loadPersistentStores { _, error in
                        if let error = error {
                            fatalError("Core Data加载失败: \\(error)")
                        }
                    }
                    return container
                }()
                
                func saveContext() {
                    let context = persistentContainer.viewContext
                    if context.hasChanges {
                        do {
                            try context.save()
                        } catch {
                            print("保存失败: \\(error)")
                        }
                    }
                }
            }
            
            // SwiftUI集成
            struct PersistenceController {
                static let shared = PersistenceController()
                
                let container: NSPersistentCloudKitContainer
                
                init() {
                    container = NSPersistentCloudKitContainer(name: "Model")
                    
                    container.loadPersistentStores { _, error in
                        if let error = error {
                            fatalError("Core Data加载失败: \\(error)")
                        }
                    }
                    
                    container.viewContext.automaticallyMergesChangesFromParent = true
                }
            }
            """, language="swift")

    # 添加App Clips支持
    st.header("App Clips")

    clip_col1, clip_col2 = st.columns(2)

    with clip_col1:
        with st.expander("App Clips配置", expanded=True):
            st.code("""
            // Info.plist配置
            /*
            <key>NSAppClipRequestEphemeralUserNotification</key>
            <true/>
            <key>NSAppClipRequestLocationConfirmation</key>
            <true/>
            */
            
            // App Clip入口
            @main
            struct AppClip: App {
                var body: some Scene {
                    WindowGroup {
                        ContentView()
                            .onContinueUserActivity(
                                NSUserActivityTypeBrowsingWeb
                            ) { userActivity in
                                // 处理App Clip启动
                                handleActivity(userActivity)
                            }
                    }
                }
            }
            """, language="swift")

    with clip_col2:
        with st.expander("App Clips功能", expanded=True):
            st.code("""
            class AppClipHandler {
                func handleActivity(_ activity: NSUserActivity) {
                    guard let incomingURL = activity.webpageURL else {
                        return
                    }
                    
                    // 解析URL参数
                    let components = URLComponents(
                        url: incomingURL,
                        resolvingAgainstBaseURL: true
                    )
                    
                    // 处理App Clip特定功能
                    if let itemID = components?.queryItems?
                        .first(where: { $0.name == "id" })?
                        .value {
                        loadItem(id: itemID)
                    }
                }
                
                func loadItem(id: String) {
                    // 加载相关内容
                }
            }
            """, language="swift")

# Tab 10 - 系统功能
with tab10:
    left_col, right_col = st.columns(2)
    
    # 左栏 - AR功能
    with left_col:
        st.header("AR功能")
        
        # ARKit基础
        with st.expander("ARKit基础", expanded=True):
            st.code("""
            struct ARView: UIViewRepresentable {
                func makeUIView(context: Context) -> ARSCNView {
                    let arView = ARSCNView()
                    
                    // 配置AR会话
                    let configuration = ARWorldTrackingConfiguration()
                    configuration.planeDetection = .horizontal
                    
                    arView.session.run(configuration)
                    arView.delegate = context.coordinator
                    
                    return arView
                }
                
                func updateUIView(_ uiView: ARSCNView, context: Context) {}
                
                func makeCoordinator() -> Coordinator {
                    Coordinator(self)
                }
                
                class Coordinator: NSObject, ARSCNViewDelegate {
                    var parent: ARView
                    
                    init(_ parent: ARView) {
                        self.parent = parent
                    }
                    
                    func renderer(_ renderer: SCNSceneRenderer, 
                                didAdd node: SCNNode,
                                for anchor: ARAnchor) {
                        // 处理添加的锚点
                        if let planeAnchor = anchor as? ARPlaneAnchor {
                            // 创建平面可视化
                            let plane = SCNPlane(
                                width: CGFloat(planeAnchor.extent.x),
                                height: CGFloat(planeAnchor.extent.z)
                            )
                            
                            let planeNode = SCNNode(geometry: plane)
                            planeNode.position = SCNVector3(
                                planeAnchor.center.x,
                                0,
                                planeAnchor.center.z
                            )
                            
                            node.addChildNode(planeNode)
                        }
                    }
                }
            }
            """, language="swift")
        
        # RealityKit
        with st.expander("RealityKit", expanded=True):
            st.code("""
            struct RealityKitView: UIViewRepresentable {
                func makeUIView(context: Context) -> ARView {
                    let arView = ARView(frame: .zero)
                    
                    // 加载3D模型
                    let anchor = try! Experience.loadBox()
                    arView.scene.anchors.append(anchor)
                    
                    return arView
                }
                
                func updateUIView(_ uiView: ARView, context: Context) {}
            }
            
            // 自定义AR体验
            class CustomARExperience: Experience {
                required init() {
                    super.init()
                    
                    // 添加手势识别
                    let tapRecognizer = UITapGestureRecognizer(
                        target: self,
                        action: #selector(handleTap)
                    )
                    self.view?.addGestureRecognizer(tapRecognizer)
                }
                
                @objc func handleTap(_ recognizer: UITapGestureRecognizer) {
                    // 处理点击事件
                }
            }
            """, language="swift")
    
    # 右栏 - 地图功能
    with right_col:
        st.header("地图功能")
        
        # 地图基础
        with st.expander("地图基础", expanded=True):
            st.code("""
            struct MapView: View {
                @State private var region = MKCoordinateRegion(
                    center: CLLocationCoordinate2D(
                        latitude: 37.334_900,
                        longitude: -122.009_020
                    ),
                    span: MKCoordinateSpan(
                        latitudeDelta: 0.2,
                        longitudeDelta: 0.2
                    )
                )
                
                var body: some View {
                    Map(coordinateRegion: $region,
                        showsUserLocation: true,
                        userTrackingMode: .follow,
                        annotationItems: locations) { location in
                        MapMarker(
                            coordinate: location.coordinate,
                            tint: .red
                        )
                    }
                }
            }
            
            // 自定义标注
            struct CustomAnnotation: View {
                var body: some View {
                    VStack {
                        Image(systemName: "mappin.circle.fill")
                            .foregroundColor(.red)
                        Text("Location")
                            .font(.caption)
                    }
                }
            }
            """, language="swift")
        
        # 路线规划
        with st.expander("路线规划", expanded=True):
            st.code("""
            class RouteManager {
                func calculateRoute(
                    from source: CLLocationCoordinate2D,
                    to destination: CLLocationCoordinate2D
                ) {
                    let request = MKDirections.Request()
                    request.source = MKMapItem(
                        placemark: MKPlacemark(coordinate: source)
                    )
                    request.destination = MKMapItem(
                        placemark: MKPlacemark(coordinate: destination)
                    )
                    
                    let directions = MKDirections(request: request)
                    directions.calculate { response, error in
                        if let route = response?.routes.first {
                            // 显示路线
                            self.showRoute(route)
                        }
                    }
                }
                
                func showRoute(_ route: MKRoute) {
                    // 在地图上绘制路线
                }
            }
            """, language="swift")

    # 添加相机和照片库
    st.header("相机和照片库")

    camera_col1, camera_col2 = st.columns(2)

    with camera_col1:
        with st.expander("相机集成", expanded=True):
            st.code("""
            struct CameraView: UIViewControllerRepresentable {
                @Binding var image: UIImage?
                @Environment(\\.presentationMode) var presentationMode
                
                func makeUIViewController(
                    context: UIViewControllerRepresentableContext<CameraView>
                ) -> UIImagePickerController {
                    let picker = UIImagePickerController()
                    picker.delegate = context.coordinator
                    picker.sourceType = .camera
                    return picker
                }
                
                func updateUIViewController(
                    _ uiViewController: UIImagePickerController,
                    context: UIViewControllerRepresentableContext<CameraView>
                ) {}
                
                func makeCoordinator() -> Coordinator {
                    Coordinator(self)
                }
                
                class Coordinator: NSObject, 
                                UINavigationControllerDelegate,
                                UIImagePickerControllerDelegate {
                    let parent: CameraView
                    
                    init(_ parent: CameraView) {
                        self.parent = parent
                    }
                    
                    func imagePickerController(
                        _ picker: UIImagePickerController,
                        didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]
                    ) {
                        if let image = info[.originalImage] as? UIImage {
                            parent.image = image
                        }
                        parent.presentationMode.wrappedValue.dismiss()
                    }
                }
            }
            """, language="swift")

    with camera_col2:
        with st.expander("照片库访问", expanded=True):
            st.code("""
            struct PhotoPicker: UIViewControllerRepresentable {
                @Binding var selectedImages: [UIImage]
                
                func makeUIViewController(
                    context: Context
                ) -> PHPickerViewController {
                    var config = PHPickerConfiguration()
                    config.selectionLimit = 0  // 0表示无限制
                    config.filter = .images
                    
                    let picker = PHPickerViewController(configuration: config)
                    picker.delegate = context.coordinator
                    return picker
                }
                
                func updateUIViewController(
                    _ uiViewController: PHPickerViewController,
                    context: Context
                ) {}
                
                func makeCoordinator() -> Coordinator {
                    Coordinator(self)
                }
                
                class Coordinator: PHPickerViewControllerDelegate {
                    let parent: PhotoPicker
                    
                    init(_ parent: PhotoPicker) {
                        self.parent = parent
                    }
                    
                    func picker(
                        _ picker: PHPickerViewController,
                        didFinishPicking results: [PHPickerResult]
                    ) {
                        for result in results {
                            result.itemProvider
                                .loadObject(ofClass: UIImage.self) { image, error in
                                if let image = image as? UIImage {
                                    DispatchQueue.main.async {
                                        self.parent.selectedImages.append(image)
                                    }
                                }
                            }
                        }
                        
                        picker.dismiss(animated: true)
                    }
                }
            }
            """, language="swift")

# Tab 11 - 高级功能
with tab11:
    left_col, right_col = st.columns(2)
    
    # 左栏 - HealthKit
    with left_col:
        st.header("HealthKit")
        
        # 健康数据访问
        with st.expander("健康数据访问", expanded=True):
            st.code("""
            class HealthKitManager {
                let healthStore = HKHealthStore()
                
                func requestAuthorization() {
                    // 定义需要读取的数据类型
                    let types = Set([
                        HKObjectType.quantityType(
                            forIdentifier: .stepCount
                        )!,
                        HKObjectType.quantityType(
                            forIdentifier: .heartRate
                        )!
                    ])
                    
                    // 请求权限
                    healthStore.requestAuthorization(
                        toShare: types,
                        read: types
                    ) { success, error in
                        if success {
                            print("HealthKit授权成功")
                        }
                    }
                }
                
                func fetchStepCount(completion: @escaping (Double) -> Void) {
                    let stepType = HKQuantityType.quantityType(
                        forIdentifier: .stepCount
                    )!
                    
                    let query = HKStatisticsQuery(
                        quantityType: stepType,
                        quantitySamplePredicate: nil,
                        options: .cumulativeSum
                    ) { _, result, _ in
                        guard let sum = result?.sumQuantity() else {
                            return
                        }
                        
                        let steps = sum.doubleValue(
                            for: HKUnit.count()
                        )
                        completion(steps)
                    }
                    
                    healthStore.execute(query)
                }
            }
            """, language="swift")
        
        # 健康数据写入
        with st.expander("健康数据写入", expanded=True):
            st.code("""
            extension HealthKitManager {
                func saveWorkout(
                    startDate: Date,
                    endDate: Date,
                    calories: Double,
                    distance: Double
                ) {
                    // 创建运动数据
                    let workout = HKWorkout(
                        activityType: .running,
                        start: startDate,
                        end: endDate,
                        duration: endDate.timeIntervalSince(startDate),
                        totalEnergyBurned: HKQuantity(
                            unit: .kilocalorie(),
                            doubleValue: calories
                        ),
                        totalDistance: HKQuantity(
                            unit: .meter(),
                            doubleValue: distance
                        ),
                        metadata: nil
                    )
                    
                    // 保存到HealthKit
                    healthStore.save(workout) { success, error in
                        if success {
                            print("运动数据保存成功")
                        }
                    }
                }
            }
            """, language="swift")
    
    # 右栏 - Apple Pay
    with right_col:
        st.header("Apple Pay")
        
        # 支付功能
        with st.expander("支付功能", expanded=True):
            st.code("""
            class PaymentHandler {
                func processPayment(amount: Decimal) {
                    // 创建支付请求
                    let request = PKPaymentRequest()
                    request.merchantIdentifier = "merchant.com.example"
                    request.supportedNetworks = [.visa, .masterCard]
                    request.merchantCapabilities = .capability3DS
                    request.countryCode = "US"
                    request.currencyCode = "USD"
                    
                    // 添加支付项目
                    request.paymentSummaryItems = [
                        PKPaymentSummaryItem(
                            label: "商品总额",
                            amount: NSDecimalNumber(decimal: amount)
                        )
                    ]
                    
                    // 显示支付界面
                    let controller = PKPaymentAuthorizationViewController(
                        paymentRequest: request
                    )
                    controller?.delegate = self
                    
                    if let controller = controller {
                        UIApplication.shared.windows.first?
                            .rootViewController?
                            .present(controller, animated: true)
                    }
                }
            }
            
            extension PaymentHandler: PKPaymentAuthorizationViewControllerDelegate {
                func paymentAuthorizationViewControllerDidFinish(
                    _ controller: PKPaymentAuthorizationViewController
                ) {
                    controller.dismiss(animated: true)
                }
                
                func paymentAuthorizationViewController(
                    _ controller: PKPaymentAuthorizationViewController,
                    didAuthorizePayment payment: PKPayment,
                    handler completion: @escaping (PKPaymentAuthorizationResult) -> Void
                ) {
                    // 处理支付结果
                    completion(PKPaymentAuthorizationResult(
                        status: .success,
                        errors: nil
                    ))
                }
            }
            """, language="swift")
        
        # 支付按钮
        with st.expander("支付按钮", expanded=True):
            st.code("""
            struct ApplePayButton: UIViewRepresentable {
                let action: () -> Void
                
                func makeUIView(context: Context) -> PKPaymentButton {
                    let button = PKPaymentButton(
                        paymentButtonType: .buy,
                        paymentButtonStyle: .black
                    )
                    button.addTarget(
                        context.coordinator,
                        action: #selector(Coordinator.buttonTapped),
                        for: .touchUpInside
                    )
                    return button
                }
                
                func updateUIView(
                    _ uiView: PKPaymentButton,
                    context: Context
                ) {}
                
                func makeCoordinator() -> Coordinator {
                    Coordinator(action: action)
                }
                
                class Coordinator: NSObject {
                    let action: () -> Void
                    
                    init(action: @escaping () -> Void) {
                        self.action = action
                    }
                    
                    @objc func buttonTapped() {
                        action()
                    }
                }
            }
            """, language="swift")

    # 添加Sign in with Apple
    st.header("Sign in with Apple")

    signin_col1, signin_col2 = st.columns(2)

    with signin_col1:
        with st.expander("登录功能", expanded=True):
            st.code("""
            struct SignInWithAppleButton: UIViewRepresentable {
                @Environment(\\.colorScheme) var colorScheme
                let onCompletion: (Result<ASAuthorizationAppleIDCredential, Error>) -> Void
                
                func makeUIView(context: Context) -> ASAuthorizationAppleIDButton {
                    let button = ASAuthorizationAppleIDButton(
                        type: .signIn,
                        style: colorScheme == .dark ? .white : .black
                    )
                    button.addTarget(
                        context.coordinator,
                        action: #selector(Coordinator.handleAuthorizationAppleIDButtonPress),
                        for: .touchUpInside
                    )
                    return button
                }
                
                func updateUIView(
                    _ uiView: ASAuthorizationAppleIDButton,
                    context: Context
                ) {}
                
                func makeCoordinator() -> Coordinator {
                    Coordinator(onCompletion: onCompletion)
                }
                
                class Coordinator: NSObject, ASAuthorizationControllerDelegate {
                    let onCompletion: (Result<ASAuthorizationAppleIDCredential, Error>) -> Void
                    
                    init(onCompletion: @escaping (Result<ASAuthorizationAppleIDCredential, Error>) -> Void) {
                        self.onCompletion = onCompletion
                    }
                    
                    @objc func handleAuthorizationAppleIDButtonPress() {
                        let request = ASAuthorizationAppleIDProvider()
                            .createRequest()
                        request.requestedScopes = [.fullName, .email]
                        
                        let controller = ASAuthorizationController(
                            authorizationRequests: [request]
                        )
                        controller.delegate = self
                        controller.performRequests()
                    }
                    
                    func authorizationController(
                        controller: ASAuthorizationController,
                        didCompleteWithAuthorization authorization: ASAuthorization
                    ) {
                        if let appleIDCredential = authorization.credential
                            as? ASAuthorizationAppleIDCredential {
                            onCompletion(.success(appleIDCredential))
                        }
                    }
                    
                    func authorizationController(
                        controller: ASAuthorizationController,
                        didCompleteWithError error: Error
                    ) {
                        onCompletion(.failure(error))
                    }
                }
            }
            """, language="swift")

    with signin_col2:
        with st.expander("用户状态管理", expanded=True):
            st.code("""
            class AuthenticationManager: ObservableObject {
                @Published var isAuthenticated = false
                @Published var userID: String?
                
                func handleSignInWithApple(
                    credential: ASAuthorizationAppleIDCredential
                ) {
                    // 获取用户标识符
                    let userID = credential.user
                    
                    // 获取身份令牌
                    if let tokenData = credential.identityToken,
                    let token = String(data: tokenData, encoding: .utf8) {
                        print("Identity Token: \\(token)")
                    }
                    
                    // 获取用户信息
                    if let email = credential.email {
                        print("Email: \\(email)")
                    }
                    
                    if let fullName = credential.fullName {
                        let firstName = fullName.givenName ?? ""
                        let lastName = fullName.familyName ?? ""
                        print("Name: \\(firstName) \\(lastName)")
                    }
                    
                    // 更新认证状态
                    DispatchQueue.main.async {
                        self.isAuthenticated = true
                        self.userID = userID
                    }
                }
                
                func signOut() {
                    DispatchQueue.main.async {
                        self.isAuthenticated = false
                        self.userID = nil
                    }
                }
            }
            """, language="swift")


with tab12:
    # 添加语音识别
    st.header("语音和机器学习")

    speech_col1, speech_col2 = st.columns(2)

    with speech_col1:
        with st.expander("语音识别", expanded=True):
            st.code("""
            class SpeechRecognizer: ObservableObject {
                private let speechRecognizer = SFSpeechRecognizer(locale: Locale(identifier: "zh-CN"))
                private var recognitionRequest: SFSpeechAudioBufferRecognitionRequest?
                private var recognitionTask: SFSpeechRecognitionTask?
                private let audioEngine = AVAudioEngine()
                
                @Published var transcript = ""
                @Published var isRecording = false
                
                func startRecording() throws {
                    // 重置之前的任务
                    recognitionTask?.cancel()
                    recognitionTask = nil
                    
                    // 配置音频会话
                    let audioSession = AVAudioSession.sharedInstance()
                    try audioSession.setCategory(.record, mode: .measurement, options: .duckOthers)
                    try audioSession.setActive(true, options: .notifyOthersOnDeactivation)
                    
                    recognitionRequest = SFSpeechAudioBufferRecognitionRequest()
                    
                    // 配置音频输入
                    let inputNode = audioEngine.inputNode
                    recognitionRequest?.shouldReportPartialResults = true
                    
                    // 开始识别
                    recognitionTask = speechRecognizer?.recognitionTask(
                        with: recognitionRequest!
                    ) { [weak self] result, error in
                        guard let self = self else { return }
                        
                        if let result = result {
                            self.transcript = result.bestTranscription.formattedString
                        }
                        
                        if error != nil {
                            self.stopRecording()
                        }
                    }
                    
                    // 安装音频tap
                    let recordingFormat = inputNode.outputFormat(forBus: 0)
                    inputNode.installTap(
                        onBus: 0,
                        bufferSize: 1024,
                        format: recordingFormat
                    ) { buffer, _ in
                        self.recognitionRequest?.append(buffer)
                    }
                    
                    audioEngine.prepare()
                    try audioEngine.start()
                    isRecording = true
                }
                
                func stopRecording() {
                    audioEngine.stop()
                    audioEngine.inputNode.removeTap(onBus: 0)
                    recognitionRequest?.endAudio()
                    isRecording = false
                }
            }
            """, language="swift")

    with speech_col2:
        with st.expander("Core ML集成", expanded=True):
            st.code("""
            class ImageClassifier: ObservableObject {
                @Published var classification: String = ""
                
                private var model: VNCoreMLModel?
                
                init() {
                    // 加载Core ML模型
                    do {
                        let config = MLModelConfiguration()
                        let imageClassifier = try MobileNetV2(configuration: config)
                        model = try VNCoreMLModel(for: imageClassifier.model)
                    } catch {
                        print("模型加载失败: \\(error)")
                    }
                }
                
                func classify(_ image: UIImage) {
                    guard let ciImage = CIImage(image: image),
                        let model = model else { return }
                    
                    // 创建图像分析请求
                    let request = VNCoreMLRequest(model: model) { [weak self] request, error in
                        guard let results = request.results as? [VNClassificationObservation],
                            let topResult = results.first else { return }
                        
                        DispatchQueue.main.async {
                            self?.classification = "
                                类别: \\(topResult.identifier)
                                置信度: \\(topResult.confidence)
                                "
                        }
                    }
                    
                    // 执行请求
                    let handler = VNImageRequestHandler(ciImage: ciImage)
                    do {
                        try handler.perform([request])
                    } catch {
                        print("分析失败: \\(error)")
                    }
                }
            }
            
            // SwiftUI视图
            struct ImageClassifierView: View {
                @StateObject private var classifier = ImageClassifier()
                @State private var selectedImage: UIImage?
                @State private var showingImagePicker = false
                
                var body: some View {
                    VStack {
                        if let image = selectedImage {
                            Image(uiImage: image)
                                .resizable()
                                .scaledToFit()
                            
                            Text(classifier.classification)
                                .padding()
                        }
                        
                        Button("选择图片") {
                            showingImagePicker = true
                        }
                    }
                    .sheet(isPresented: $showingImagePicker) {
                        ImagePicker(image: $selectedImage)
                    }
                    .onChange(of: selectedImage) { newImage in
                        if let image = newImage {
                            classifier.classify(image)
                        }
                    }
                }
            }
            """, language="swift")

    # 添加Metal图形处理
    st.header("Metal图形处理")

    metal_col1, metal_col2 = st.columns(2)

    with metal_col1:
        with st.expander("Metal基础", expanded=True):
            st.code("""
            class MetalRenderer {
                private let device: MTLDevice
                private let commandQueue: MTLCommandQueue
                private var pipeline: MTLRenderPipelineState
                
                init() {
                    guard let device = MTLCreateSystemDefaultDevice(),
                        let commandQueue = device.makeCommandQueue() else {
                        fatalError("Metal初始化失败")
                    }
                    
                    self.device = device
                    self.commandQueue = commandQueue
                    
                    // 创建渲染管线
                    let library = device.makeDefaultLibrary()!
                    let vertexFunction = library.makeFunction(name: "vertexShader")
                    let fragmentFunction = library.makeFunction(name: "fragmentShader")
                    
                    let pipelineDescriptor = MTLRenderPipelineDescriptor()
                    pipelineDescriptor.vertexFunction = vertexFunction
                    pipelineDescriptor.fragmentFunction = fragmentFunction
                    pipelineDescriptor.colorAttachments[0].pixelFormat = .bgra8Unorm
                    
                    do {
                        pipeline = try device.makeRenderPipelineState(
                            descriptor: pipelineDescriptor
                        )
                    } catch {
                        fatalError("管线创建失败: \\(error)")
                    }
                }
                
                func render(in view: MTKView) {
                    guard let commandBuffer = commandQueue.makeCommandBuffer(),
                        let descriptor = view.currentRenderPassDescriptor,
                        let encoder = commandBuffer.makeRenderCommandEncoder(
                            descriptor: descriptor
                        ) else { return }
                    
                    encoder.setRenderPipelineState(pipeline)
                    // 设置顶点数据和绘制命令
                    encoder.endEncoding()
                    
                    if let drawable = view.currentDrawable {
                        commandBuffer.present(drawable)
                    }
                    
                    commandBuffer.commit()
                }
            }
            """, language="swift")

    with metal_col2:
        with st.expander("Metal着色器", expanded=True):
            st.code("""
            // Metal着色器代码 (.metal文件)
            #include <metal_stdlib>
            using namespace metal;
            
            struct VertexIn {
                float3 position [[attribute(0)]];
                float2 texCoord [[attribute(1)]];
    };
            
            struct VertexOut {
                float4 position [[position]];
                float2 texCoord;
            };
            
            vertex VertexOut vertexShader(
                const VertexIn vertex [[stage_in]]
            ) {
                VertexOut out;
                out.position = float4(vertex.position, 1.0);
                out.texCoord = vertex.texCoord;
                return out;
            }
            
            fragment float4 fragmentShader(
                VertexOut in [[stage_in]],
                texture2d<float> texture [[texture(0)]],
                sampler textureSampler [[sampler(0)]]
            ) {
                float4 color = texture.sample(
                    textureSampler,
                    in.texCoord
                );
                return color;
            }
            """, language="metal")

    # 添加文件系统操作
    st.header("文件系统操作")

    file_col1, file_col2 = st.columns(2)

    with file_col1:
        with st.expander("文件管理", expanded=True):
            st.code("""
            class FileManager {
                static let shared = FileManager()
                
                // 获取文档目录
                var documentsDirectory: URL {
                    FileManager.default.urls(
                        for: .documentDirectory,
                        in: .userDomainMask
                    )[0]
                }
                
                // 保存数据
                func saveData(_ data: Data, to filename: String) throws {
                    let url = documentsDirectory.appendingPathComponent(filename)
                    try data.write(to: url)
                }
                
                // 读取数据
                func loadData(from filename: String) throws -> Data {
                    let url = documentsDirectory.appendingPathComponent(filename)
                    return try Data(contentsOf: url)
                }
                
                // 删除文件
                func deleteFile(_ filename: String) throws {
                    let url = documentsDirectory.appendingPathComponent(filename)
                    try FileManager.default.removeItem(at: url)
                }
                
                // 列出文件
                func listFiles() throws -> [String] {
                    try FileManager.default.contentsOfDirectory(
                        atPath: documentsDirectory.path
                    )
                }
            }
            """, language="swift")

    with file_col2:
        with st.expander("文档选择器", expanded=True):
            st.code("""
            struct DocumentPicker: UIViewControllerRepresentable {
                let onDocumentsPicked: ([URL]) -> Void
                
                func makeUIViewController(
                    context: Context
                ) -> UIDocumentPickerViewController {
                    let picker = UIDocumentPickerViewController(
                        forOpeningContentTypes: [.pdf, .text],
                        asCopy: true
                    )
                    picker.delegate = context.coordinator
                    picker.allowsMultipleSelection = true
                    return picker
                }
                
                func updateUIViewController(
                    _ uiViewController: UIDocumentPickerViewController,
                    context: Context
                ) {}
                
                func makeCoordinator() -> Coordinator {
                    Coordinator(onDocumentsPicked: onDocumentsPicked)
                }
                
                class Coordinator: NSObject, UIDocumentPickerDelegate {
                    let onDocumentsPicked: ([URL]) -> Void
                    
                    init(onDocumentsPicked: @escaping ([URL]) -> Void) {
                        self.onDocumentsPicked = onDocumentsPicked
                    }
                    
                    func picker(
                        _ picker: UIDocumentPickerViewController,
                        didFinishPicking results: [UIDocumentPickerResult]
                    ) {
                        for result in results {
                            result.itemProvider
                                .loadObject(ofClass: UIImage.self) { image, error in
                                if let image = image as? UIImage {
                                    DispatchQueue.main.async {
                                        self.parent.selectedImages.append(image)
                                    }
                                }
                            }
                        }
                        
                        picker.dismiss(animated: true)
                    }
                }
            }
            """, language="swift")


with tab13:
    # 添加网络安全
    st.header("网络安全")

    security_col1, security_col2 = st.columns(2)

    with security_col1:
        with st.expander("加密解密", expanded=True):
            st.code("""
            class CryptoManager {
                // AES 加密
                func encrypt(_ string: String, with key: String) throws -> Data {
                    let keyData = key.data(using: .utf8)!
                    let stringData = string.data(using: .utf8)!
                    
                    let symmetricKey = SymmetricKey(data: keyData)
                    let sealedBox = try AES.GCM.seal(
                        stringData,
                        using: symmetricKey
                    )
                    
                    return sealedBox.combined!
                }
                
                // AES 解密
                func decrypt(_ data: Data, with key: String) throws -> String {
                    let keyData = key.data(using: .utf8)!
                    let symmetricKey = SymmetricKey(data: keyData)
                    
                    let sealedBox = try AES.GCM.SealedBox(combined: data)
                    let decryptedData = try AES.GCM.open(
                        sealedBox,
                        using: symmetricKey
                    )
                    
                    return String(data: decryptedData, encoding: .utf8)!
                }
                
                // 密钥生成
                func generateKey() -> String {
                    let key = SymmetricKey(size: .bits256)
                    return Data(key.withUnsafeBytes { Data($0) })
                        .base64EncodedString()
                }
            }
            """, language="swift")

    with security_col2:
        with st.expander("安全存储", expanded=True):
            st.code("""
            class KeychainManager {
                enum KeychainError: Error {
                    case duplicateEntry
                    case unknown(OSStatus)
                }
                
                // 保存到钥匙串
                func save(
                    password: String,
                    for account: String,
                    service: String
                ) throws {
                    let passwordData = password.data(using: .utf8)!
                    
                    let query: [String: Any] = [
                        kSecClass as String: kSecClassGenericPassword,
                        kSecAttrAccount as String: account,
                        kSecAttrService as String: service,
                        kSecValueData as String: passwordData
                    ]
                    
                    let status = SecItemAdd(query as CFDictionary, nil)
                    
                    guard status != errSecDuplicateItem else {
                        throw KeychainError.duplicateEntry
                    }
                    
                    guard status == errSecSuccess else {
                        throw KeychainError.unknown(status)
                    }
                }
                
                // 从钥匙串读取
                func retrieve(
                    account: String,
                    service: String
                ) throws -> String? {
                    let query: [String: Any] = [
                        kSecClass as String: kSecClassGenericPassword,
                        kSecAttrAccount as String: account,
                        kSecAttrService as String: service,
                        kSecReturnData as String: true
                    ]
                    
                    var result: AnyObject?
                    let status = SecItemCopyMatching(
                        query as CFDictionary,
                        &result
                    )
                    
                    guard status == errSecSuccess else {
                        return nil
                    }
                    
                    guard let passwordData = result as? Data,
                        let password = String(
                            data: passwordData,
                            encoding: .utf8
                        ) else {
                        return nil
                    }
                    
                    return password
                }
            }
            """, language="swift")

    # 添加推送通知高级功能
    st.header("推送通知高级功能")

    push_col1, push_col2 = st.columns(2)

    with push_col1:
        with st.expander("富文本通知", expanded=True):
            st.code("""
            class NotificationService: UNNotificationServiceExtension {
                override func didReceive(
                    _ request: UNNotificationRequest,
                    withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void
                ) {
                    guard let bestAttemptContent = 
                        request.content.mutableCopy() 
                            as? UNMutableNotificationContent else {
                        contentHandler(request.content)
                        return
                    }
                    
                    // 添加媒体附件
                    if let imageURLString = 
                        bestAttemptContent.userInfo["image_url"] as? String,
                    let imageURL = URL(string: imageURLString) {
                        
                        downloadAndAttach(
                            url: imageURL,
                            to: bestAttemptContent,
                            withIdentifier: "image"
                        ) { content in
                            contentHandler(content)
                        }
                    }
                }
                
                func downloadAndAttach(
                    url: URL,
                    to content: UNMutableNotificationContent,
                    withIdentifier identifier: String,
                    completion: @escaping (UNNotificationContent) -> Void
                ) {
                    let task = URLSession.shared.downloadTask(with: url) { 
                        location, _, error in
                        
                        guard let location = location else {
                            completion(content)
                            return
                        }
                        
                        let tmpDirectory = URL(
                            fileURLWithPath: NSTemporaryDirectory()
                        )
                        let tmpFile = tmpDirectory.appendingPathComponent(
                            identifier
                        )
                        
                        try? FileManager.default.moveItem(
                            at: location,
                            to: tmpFile
                        )
                        
                        if let attachment = try? UNNotificationAttachment(
                            identifier: identifier,
                            url: tmpFile
                        ) {
                            content.attachments = [attachment]
                        }
                        
                        completion(content)
                    }
                    task.resume()
                }
            }
            """, language="swift")

    with push_col2:
        with st.expander("通知操作", expanded=True):
            st.code("""
            class NotificationManager {
                func setupNotificationCategories() {
                    // 定义操作
                    let acceptAction = UNNotificationAction(
                        identifier: "ACCEPT_ACTION",
                        title: "接受",
                        options: .foreground
                    )
                    
                    let declineAction = UNNotificationAction(
                        identifier: "DECLINE_ACTION",
                        title: "拒绝",
                        options: [.destructive, .foreground]
                    )
                    
                    let textInputAction = UNTextInputNotificationAction(
                        identifier: "TEXT_ACTION",
                        title: "回复",
                        options: [],
                        textInputButtonTitle: "发送",
                        textInputPlaceholder: "输入回复..."
                    )
                    
                    // 创建类别
                    let category = UNNotificationCategory(
                        identifier: "MEETING_INVITATION",
                        actions: [acceptAction, declineAction, textInputAction],
                        intentIdentifiers: [],
                        hiddenPreviewsBodyPlaceholder: "新的会议邀请",
                        options: .customDismissAction
                    )
                    
                    // 注册类别
                    UNUserNotificationCenter.current()
                        .setNotificationCategories([category])
                }
                
                // 处理通知响应
                func handleNotificationResponse(
                    _ response: UNNotificationResponse
                ) {
                    switch response.actionIdentifier {
                    case "ACCEPT_ACTION":
                        handleAccept(response.notification)
                        
                    case "DECLINE_ACTION":
                        handleDecline(response.notification)
                        
                    case "TEXT_ACTION":
                        if let textResponse = response as? UNTextInputNotificationResponse {
                            handleReply(
                                response.notification,
                                text: textResponse.userText
                            )
                        }
                        
                    default:
                        break
                    }
                }
            }
            """, language="swift")

    # 添加应用间通信
    st.header("应用间通信")

    app_col1, app_col2 = st.columns(2)

    with app_col1:
        with st.expander("URL Schemes", expanded=True):
            st.code("""
            class DeepLinkHandler {
                func handle(url: URL) {
                    guard let components = URLComponents(
                        url: url,
                        resolvingAgainstBaseURL: true
                    ) else { return }
                    
                    // 解析路径
                    switch components.path {
                    case "/product":
                        if let productId = components.queryItems?
                            .first(where: { $0.name == "id" })?
                            .value {
                            openProduct(id: productId)
                        }
                        
                    case "/search":
                        if let query = components.queryItems?
                            .first(where: { $0.name == "q" })?
                            .value {
                            performSearch(query: query)
                        }
                        
                    default:
                        break
                    }
                }
                
                // Info.plist配置
                /*
                <key>CFBundleURLTypes</key>
                <array>
                    <dict>
                        <key>CFBundleURLSchemes</key>
                        <array>
                            <string>myapp</string>
                        </array>
                    </dict>
                </array>
                */
            }
            """, language="swift")

    with app_col2:
        with st.expander("共享数据", expanded=True):
            st.code("""
            // App Groups配置
            let groupIdentifier = "group.com.example.app"
            
            class SharedDataManager {
                let userDefaults = UserDefaults(
                    suiteName: "group.com.example.app"
                )
                
                // 共享文件
                var sharedContainer: URL? {
                    FileManager.default
                        .containerURL(
                            forSecurityApplicationGroupIdentifier: groupIdentifier
                        )
                }
                
                // 保存共享数据
                func saveSharedData(_ data: Data, filename: String) throws {
                    guard let url = sharedContainer?
                        .appendingPathComponent(filename) else {
                        throw NSError(
                            domain: "SharedDataError",
                            code: -1,
                            userInfo: nil
                        )
                    }
                    
                    try data.write(to: url)
                }
                
                // 读取共享数据
                func readSharedData(filename: String) throws -> Data {
                    guard let url = sharedContainer?
                        .appendingPathComponent(filename) else {
                        throw NSError(
                            domain: "SharedDataError",
                            code: -1,
                            userInfo: nil
                        )
                    }
                    
                    return try Data(contentsOf: url)
                }
            }
            """, language="swift")



with tab14:
    st.header("系统扩展")

extension_col1, extension_col2 = st.columns(2)

with extension_col1:
    with st.expander("共享扩展", expanded=True):
        st.code("""
        class ShareViewController: SLComposeServiceViewController {
            override func isContentValid() -> Bool {
                // 验证内容是否有效
                return contentText.isEmpty == false
            }
            
            override func didSelectPost() {
                // 处理分享内容
                if let text = contentText {
                    // 处理文本
                    handleSharedText(text)
                }
                
                if let items = extensionContext?.inputItems as? [NSExtensionItem] {
                    for item in items {
                        if let attachments = item.attachments {
                            for attachment in attachments {
                                if attachment.hasItemConformingToTypeIdentifier(
                                    kUTTypeImage as String
                                ) {
                                    handleSharedImage(attachment)
                                }
                            }
                        }
                    }
                }
                
                // 完成并关闭扩展
                self.extensionContext?.completeRequest(
                    returningItems: nil,
                    completionHandler: nil
                )
            }
            
            override func configurationItems() -> [Any]! {
                // 配置选项
                let item = SLComposeSheetConfigurationItem()
                item?.title = "选项"
                item?.value = "默认"
                item?.tapHandler = {
                    // 处理选项点击
                }
                return [item!]
            }
        }
        """, language="swift")

with extension_col2:
    with st.expander("Today Widget", expanded=True):
        st.code("""
        struct WidgetView: Widget {
            private let kind: String = "MyWidget"
            
            var body: some WidgetConfiguration {
                StaticConfiguration(
                    kind: kind,
                    provider: WidgetTimelineProvider()
                ) { entry in
                    WidgetEntryView(entry: entry)
                }
                .configurationDisplayName("My Widget")
                .description("Widget description")
                .supportedFamilies([.systemSmall, .systemMedium])
            }
        }
        
        struct WidgetTimelineProvider: TimelineProvider {
            func getSnapshot(
                in context: Context,
                completion: @escaping (WidgetEntry) -> Void
            ) {
                let entry = WidgetEntry(
                    date: Date(),
                    data: "Snapshot Data"
                )
                completion(entry)
            }
            
            func getTimeline(
                in context: Context,
                completion: @escaping (Timeline<WidgetEntry>) -> Void
            ) {
                var entries: [WidgetEntry] = []
                let currentDate = Date()
                
                for hourOffset in 0 ..< 5 {
                    let entryDate = Calendar.current.date(
                        byAdding: .hour,
                        value: hourOffset,
                        to: currentDate
                    )!
                    let entry = WidgetEntry(
                        date: entryDate,
                        data: "Data \(hourOffset)"
                    )
                    entries.append(entry)
                }
                
                let timeline = Timeline(
                    entries: entries,
                    policy: .atEnd
                )
                completion(timeline)
            }
        }
        """, language="swift")

# 添加Siri集成
st.header("Siri集成")

siri_col1, siri_col2 = st.columns(2)

with siri_col1:
    with st.expander("Siri Shortcuts", expanded=True):
        st.code("""
        class ShortcutsManager {
            func donateShortcut(
                title: String,
                action: String
            ) {
                let activity = NSUserActivity(
                    activityType: "com.example.shortcut"
                )
                activity.title = title
                activity.userInfo = ["action": action]
                activity.isEligibleForSearch = true
                activity.isEligibleForPrediction = true
                
                // 添加建议短语
                activity.suggestedInvocationPhrase = "执行操作"
                
                view.userActivity = activity
                activity.becomeCurrent()
            }
            
            // 处理Shortcuts
            func handleShortcut(_ activity: NSUserActivity) {
                guard activity.activityType == "com.example.shortcut",
                      let action = activity.userInfo?["action"] as? String else {
                    return
                }
                
                // 执行操作
                performAction(action)
            }
        }
        
        // Info.plist配置
        /*
        <key>NSUserActivityTypes</key>
        <array>
            <string>com.example.shortcut</string>
        </array>
        */
        """, language="swift")

with siri_col2:
    with st.expander("Siri Intent", expanded=True):
        st.code("""
        // Intent定义
        class CustomIntent: INIntent {
            @NSManaged var parameter: String
            
            override init() {
                super.init()
            }
            
            required init?(coder: NSCoder) {
                super.init(coder: coder)
            }
        }
        
        // Intent处理
        class IntentHandler: INExtension, CustomIntentHandling {
            func handle(
                intent: CustomIntent,
                completion: @escaping (CustomIntentResponse) -> Void
            ) {
                // 处理Intent
                let response = CustomIntentResponse(
                    code: .success,
                    userActivity: nil
                )
                completion(response)
            }
            
            func resolveParameter(
                for intent: CustomIntent,
                with completion: @escaping (INStringResolutionResult) -> Void
            ) {
                guard let parameter = intent.parameter else {
                    completion(.needsValue())
                    return
                }
                
                completion(.success(with: parameter))
            }
        }
        """, language="swift")

# 添加性能优化
st.header("性能优化")

perf_col1, perf_col2 = st.columns(2)

with perf_col1:
    with st.expander("内存优化", expanded=True):
        st.code("""
        class MemoryOptimization {
            // 图片缓存
            let imageCache = NSCache<NSString, UIImage>()
            
            func loadImage(
                url: URL,
                completion: @escaping (UIImage?) -> Void
            ) {
                // 检查缓存
                if let cachedImage = imageCache.object(
                    forKey: url.absoluteString as NSString
                ) {
                    completion(cachedImage)
                    return
                }
                
                // 下载图片
                URLSession.shared.dataTask(with: url) { [weak self] data, _, _ in
                    guard let data = data,
                          let image = UIImage(data: data) else {
                        completion(nil)
                        return
                    }
                    
                    // 存入缓存
                    self?.imageCache.setObject(
                        image,
                        forKey: url.absoluteString as NSString
                    )
                    
                    completion(image)
                }.resume()
            }
            
            // 自动释放缓存
            func setupCacheLimit() {
                imageCache.countLimit = 100
                imageCache.totalCostLimit = 50 * 1024 * 1024 // 50MB
                
                NotificationCenter.default.addObserver(
                    forName: UIApplication.didReceiveMemoryWarningNotification,
                    object: nil,
                    queue: .main
                ) { [weak self] _ in
                    self?.imageCache.removeAllObjects()
                }
            }
        }
        """, language="swift")

with perf_col2:
    with st.expander("性能监控", expanded=True):
        st.code("""
        class PerformanceMonitor {
            static let shared = PerformanceMonitor()
            
            private var startTime: CFAbsoluteTime = 0
            private var measurements: [String: CFAbsoluteTime] = [:]
            
            // 开始测量
            func startMeasuring(_ identifier: String) {
                startTime = CFAbsoluteTimeGetCurrent()
            }
            
            // 结束测量
            func stopMeasuring(_ identifier: String) {
                let timeElapsed = CFAbsoluteTimeGetCurrent() - startTime
                measurements[identifier] = timeElapsed
                
                print("\\(identifier): \\(timeElapsed)s")
            }
            
            // 内存使用
            func reportMemoryUsage() {
                var info = mach_task_basic_info()
                var count = mach_msg_type_number_t(
                    MemoryLayout<mach_task_basic_info>.size/MemoryLayout<natural_t>.size
                )
                
                let kerr: kern_return_t = withUnsafeMutablePointer(to: &info) {
                    $0.withMemoryRebound(
                        to: integer_t.self,
                        capacity: 1
                    ) {
                        task_info(
                            mach_task_self_,
                            task_flavor_t(MACH_TASK_BASIC_INFO),
                            $0,
                            &count
                        )
                    }
                }
                
                if kerr == KERN_SUCCESS {
                    let usedMB = Double(info.resident_size) / 1024.0 / 1024.0
                    print("内存使用: \\(usedMB)MB")
                }
            }
        }
        """, language="swift")


with tab15:
    # 在文件开头添加索引部分
    st.title("SwiftUI 完整指南")

    # 添加简介
    st.markdown("""
    ## 📚 使用指南

    这个 SwiftUI 速查表包含了从基础到高级的所有主要功能，帮助你快速查找和学习 SwiftUI 开发知识。

    ### 🔍 内容索引
    1. **基础组件**
    - 文本和图像
    - 按钮和输入控件
    - 列表和滚动视图
    
    2. **导航和布局**
    - 导航视图
    - 标签视图
    - 栈布局
    - 网格布局
    
    3. **状态和动画**
    - 状态管理
    - 数据流
    - 基础动画
    - 高级动画效果
    
    4. **高级特性**
    - 自定义视图
    - 手势识别
    - 绘图和形状
    - 视图修饰符

    5. **系统集成**
    - 通知处理
    - 后台任务
    - 数据持久化
    - 网络请求

    6. **平台特性**
    - iOS 特性
    - macOS 适配
    - watchOS 开发
    - iPadOS 多任务

    7. **性能和优化**
    - 内存管理
    - 性能监控
    - 调试技巧
    - 最佳实践
    """)

    # 添加快速跳转
    st.markdown("""
    ### ⚡ 快速跳转

    - [基础组件](#基础组件)
    - [布局系统](#导航和布局)
    - [状态管理](#状态和动画)
    - [高级功能](#高级特性)
    - [系统集成](#系统集成)
    - [平台特性](#平台特性)
    - [性能优化](#性能和优化)
    """)

    # 添加最佳实践总结
    st.markdown("""
    ## 💡 最佳实践总结

    ### 架构设计
    1. **遵循 MVVM 模式**
    - 将业务逻辑从视图中分离
    - 使用 ObservableObject 管理状态
    - 保持视图简单和声明式

    2. **模块化设计**
    - 组件化开发
    - 复用通用视图
    - 保持代码整洁

    ### 性能优化
    1. **视图优化**
    - 避免过度嵌套
    - 使用懒加载视图
    - 优化列表性能

    2. **内存管理**
    - 正确使用引用类型
    - 避免内存泄漏
    - 及时释放资源

    ### 调试技巧
    1. **预览调试**
    - 使用多个预览配置
    - 测试不同设备尺寸
    - 暗黑模式适配

    2. **性能分析**
    - 使用 Instruments
    - 监控内存使用
    - 分析渲染性能
    """)

    # 添加常见问题解答
    st.markdown("""
    ## ❓ 常见问题解答

    ### 状态管理
    Q: 什么时候使用 @State 和 @StateObject？
    A: @State 用于简单的值类型数据，@StateObject 用于引用类型的观察对象。

    ### 视图更新
    Q: 为什么我的视图没有更新？
    A: 检查是否正确使用了状态属性包装器，确保数据模型遵循正确的协议。

    ### 性能问题
    Q: 列表滚动不流畅怎么办？
    A: 使用 LazyVStack，实现视图回收，避免重复创建视图。

    ### 生命周期
    Q: 如何处理视图的生命周期？
    A: 使用 onAppear 和 onDisappear 修饰符，必要时实现自定义的生命周期行为。
    """)

    # 添加学习资源
    st.markdown("""
    ## 📖 推荐学习资源

    ### 官方资源
    - [Apple SwiftUI 文档](https://developer.apple.com/documentation/swiftui)
    - [WWDC 视频](https://developer.apple.com/videos/)
    - [Swift 编程语言](https://docs.swift.org/swift-book/)

    ### 社区资源
    - [SwiftUI by Example](https://www.hackingwithswift.com/quick-start/swiftui)
    - [SwiftUI Lab](https://swiftui-lab.com)
    - [Swift by Sundell](https://www.swiftbysundell.com)

    ### 开源项目
    - [Awesome SwiftUI](https://github.com/vlondon/awesome-swiftui)
    - [SwiftUI 开源应用](https://github.com/topics/swiftui)
    """)

    # 添加版本更新日志
    st.markdown("""
    ## 📝 更新日志

    ### 2024 更新
    - 添加 SwiftUI 4.0 新特性
    - 更新 iOS 17 相关内容
    - 添加更多实用示例
    - 优化代码结构

    ### 计划更新
    - SwiftUI 测试最佳实践
    - 更多自定义组件示例
    - 性能优化深度指南
    - 跨平台开发实践
    """)

