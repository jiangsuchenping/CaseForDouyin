# Ruby 邮件发送示例

## 项目简介

这是一个使用Ruby语言编写的邮件发送示例程序，演示如何使用Ruby的mail库发送各种类型的邮件。

## 功能特性

- ✅ 发送纯文本邮件
- ✅ 发送HTML格式邮件  
- ✅ 发送带附件的邮件
- ✅ 安全的占位符配置
- ✅ 详细的代码注释和文档
- ✅ 面向对象的设计

## 环境要求

- Ruby 2.5 或更高版本
- mail gem
- net-smtp gem

## 依赖安装

### 安装Ruby（如果尚未安装）

#### Windows:
下载并安装 [RubyInstaller](https://rubyinstaller.org/)

#### macOS:
```bash
# 使用Homebrew
brew install ruby

# 或使用rbenv
rbenv install 3.0.0
rbenv global 3.0.0
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install ruby ruby-dev build-essential
```

### 安装依赖gem

```bash
# 安装mail和net-smtp gem
gem install mail net-smtp

# 或者使用Bundler（推荐）
# 首先创建Gemfile
cat > Gemfile << 'EOF'
source 'https://rubygems.org'

gem 'mail', '~> 2.8'
gem 'net-smtp', '~> 0.4'
EOF

# 然后安装依赖
bundle install
```

## 使用方法

### 1. 配置邮件服务器

编辑 `send_email.rb` 文件，修改以下配置：

```ruby
# 邮件服务器配置常量
SMTP_HOST = 'your.smtp.server.com'     # SMTP服务器地址
SMTP_PORT = 587                        # SMTP服务器端口
USERNAME = 'your_email@example.com'    # 发件人邮箱
PASSWORD = 'your_password'             # 发件人密码或授权码

# 邮件内容配置常量
SENDER_EMAIL = 'your_email@example.com'    # 发件人邮箱
SENDER_NAME = 'Your Name'                  # 发件人名称
RECIPIENT_EMAIL = 'recipient@example.com'    # 收件人邮箱
RECIPIENT_NAME = 'Recipient Name'          # 收件人名称
```

### 2. 运行程序

#### 基本运行：
```bash
ruby send_email.rb
```

#### 使用Bundler运行：
```bash
bundle exec ruby send_email.rb
```

#### 添加执行权限后运行（Linux/macOS）：
```bash
chmod +x send_email.rb
./send_email.rb
```

### 3. 交互式使用

您也可以在irb或pry中交互式使用：

```ruby
require './send_email'

# 创建邮件发送器
sender = EmailSender.new

# 发送纯文本邮件
sender.send_text_email

# 发送HTML邮件
sender.send_html_email

# 发送带附件的邮件
sender.send_email_with_attachment
```

## 功能演示

程序运行后会演示三种邮件发送功能：

1. **纯文本邮件** - 发送简单的文本内容
2. **HTML格式邮件** - 发送包含HTML格式的邮件
3. **带附件邮件** - 发送包含文件附件的邮件

### 示例输出：
```
Ruby 发送邮件示例
==================

注意：此示例使用占位符配置，请替换为实际配置后再发送邮件。

1. 演示发送纯文本邮件：
纯文本邮件内容已准备好：
  发件人：your_email@example.com
  收件人：recipient@example.com
  主题：Ruby 纯文本邮件测试
  正文：这是一封使用 Ruby 发送的纯文本邮件。
  （注：未实际发送，仅展示示例）

2. 演示发送HTML格式邮件：
HTML邮件内容已准备好：
  发件人：your_email@example.com
  收件人：recipient@example.com
  主题：Ruby HTML邮件测试
  HTML正文长度：XXX 字符
  （注：未实际发送，仅展示示例）

3. 演示发送带附件的邮件：
带附件的邮件内容已准备好：
  发件人：your_email@example.com
  收件人：recipient@example.com
  主题：Ruby 带附件邮件测试
  正文：这是一封带附件的邮件，附件为测试文件。
  已添加附件：hundred_chickens.rb
  （注：未实际发送，仅展示示例）

所有演示完成！
```

## 类和方法说明

### EmailSender类

主要邮件发送器类，包含以下方法：

#### `initialize`
初始化邮件发送器，配置SMTP设置

#### `send_text_email`
发送纯文本邮件

#### `send_html_email`  
发送HTML格式邮件

#### `send_email_with_attachment`
发送带附件的邮件

## 安全提示

⚠️ **重要安全建议：**

1. **使用占位符配置** - 代码默认使用示例配置，不会暴露真实密码
2. **实际使用时请替换配置** - 将占位符替换为您的实际邮件服务器配置
3. **使用应用专用密码** - 建议使用应用专用密码而非主密码
4. **保护配置文件** - 不要将包含真实密码的代码提交到版本控制
5. **启用两步验证** - 为您的邮箱账户启用两步验证
6. **环境变量** - 考虑使用环境变量存储敏感信息

### 使用环境变量的示例：
```ruby
# 从环境变量读取配置
SMTP_HOST = ENV['SMTP_HOST'] || 'smtp.example.com'
USERNAME = ENV['SMTP_USERNAME'] || 'your_email@example.com'
PASSWORD = ENV['SMTP_PASSWORD'] || 'your_password'
```

## 常见问题

### Q: 出现 `Net::SMTPAuthenticationError`
**A:** 检查用户名和密码是否正确，确保使用的是应用专用密码（如果邮箱提供商支持）。

### Q: 出现 `SocketError: getaddrinfo: Name or service not known`
**A:** 检查SMTP服务器地址是否正确，确保网络连接正常。

### Q: 出现 `LoadError: cannot load such file -- mail`
**A:** 确保已安装mail gem：`gem install mail`

### Q: 附件文件找不到
**A:** 确保附件文件存在于程序运行的当前目录中。

### Q: 中文乱码问题
**A:** 代码已设置UTF-8编码，确保您的系统环境也使用UTF-8编码。

### Q: SSL/TLS连接问题
**A:** 检查SMTP服务器是否需要SSL/TLS，可能需要调整 `enable_starttls_auto` 设置。

## 扩展功能

您可以基于此示例扩展以下功能：
- ✅ 批量邮件发送
- ✅ 邮件模板系统（使用ERB模板）
- ✅ 邮件队列处理
- ✅ 邮件发送日志记录
- ✅ 邮件发送状态监控
- ✅ 多SMTP服务器配置
- ✅ 邮件发送重试机制

### 批量发送示例：
```ruby
def send_batch_emails(recipients, subject, body)
  recipients.each do |recipient|
    mail = Mail.new do
      from     "#{SENDER_NAME} <#{SENDER_EMAIL}>"
      to       recipient
      subject  subject
      body     body
    end
    
    # mail.deliver!
    puts "准备发送邮件给：#{recipient}"
  end
end
```

## 最佳实践

1. **错误处理** - 始终包含适当的错误处理
2. **日志记录** - 记录邮件发送活动
3. **配置管理** - 使用配置文件或环境变量
4. **测试模式** - 在开发环境中使用测试模式
5. **性能优化** - 对于大量邮件使用连接池

## 技术支持

如遇到问题，请检查：
1. Ruby版本是否符合要求
2. 依赖gem是否正确安装
3. 网络连接是否正常
4. 邮件服务器配置是否正确
5. 防火墙是否阻止了SMTP连接

## 版本历史

- **v1.0.0** (2025-12-18) - 初始版本，支持三种邮件类型发送，包含完整的文档和示例