#!/usr/bin/env ruby
# -*- coding: utf-8 -*-

# Ruby 发送邮件示例程序
#
# 项目名称：CaseForDouyin
# 模块名称：Ruby邮件发送示例
# 文件功能：演示如何使用Ruby的mail库发送邮件
#
# 功能说明：
# 1. 发送纯文本邮件
# 2. 发送HTML格式邮件
# 3. 发送带附件的邮件
#
# 依赖要求：
# - mail gem (gem install mail)
# - net-smtp gem (gem install net-smtp)
#
# 使用方法：
# 1. 安装依赖：gem install mail net-smtp
# 2. 修改邮件服务器配置（smtp_host, smtp_port, username, password）
# 3. 修改发件人和收件人邮箱地址
# 4. 运行程序：ruby send_email.rb
#
# 安全提示：
# - 使用占位符配置，避免暴露真实密码
# - 实际使用时请替换为自己的邮件服务器配置
# - 建议使用应用专用密码而非主密码
#
# @author 项目开发团队
# @version 1.0.0
# @since 2025-12-18

require 'mail'
require 'net/smtp'

# 邮件发送器类
# 负责管理邮件服务器配置和发送各种类型的邮件
#
# 设计原则：
# - 单一职责原则：每个方法只负责一种邮件类型的发送
# - 开闭原则：易于扩展新的邮件类型
# - 依赖倒置：通过模块抽象邮件发送功能
class EmailSender
  
  # 邮件服务器配置常量
  # 使用占位符，用户需要替换为实际配置
  SMTP_HOST = 'smtp.example.com'     # SMTP服务器地址
  SMTP_PORT = 587                      # SMTP服务器端口
  USERNAME = 'your_email@example.com'  # 发件人邮箱
  PASSWORD = 'your_password'           # 发件人密码或授权码
  
  # 邮件内容配置常量
  # 使用占位符，用户需要替换为实际信息
  SENDER_EMAIL = 'your_email@example.com'   # 发件人邮箱
  SENDER_NAME = '发件人名称'                   # 发件人名称
  RECIPIENT_EMAIL = 'recipient@example.com'   # 收件人邮箱
  RECIPIENT_NAME = '收件人名称'                 # 收件人名称
  
  # 类级注释
  # 初始化邮件发送器并配置邮件选项
  def initialize
    # 配置邮件发送选项
    Mail.defaults do
      delivery_method :smtp, {
        address: SMTP_HOST,
        port: SMTP_PORT,
        user_name: USERNAME,
        password: PASSWORD,
        authentication: 'plain',
        enable_starttls_auto: true,
        openssl_verify_mode: 'none'
      }
    end
  end
  
  # 发送纯文本邮件
  # 创建并发送简单的纯文本邮件
  #
  # 注意：默认注释掉实际发送代码，防止误发
  def send_text_email
    begin
      # 创建邮件
      mail = Mail.new do
        from     "#{SENDER_NAME} <#{SENDER_EMAIL}>"
        to       "#{RECIPIENT_NAME} <#{RECIPIENT_EMAIL}>"
        subject  'Ruby 纯文本邮件测试'
        body     '这是一封使用 Ruby 发送的纯文本邮件。'
      end
      
      # 显示邮件内容信息
      puts "纯文本邮件内容已准备好："
      puts "  发件人：#{SENDER_EMAIL}"
      puts "  收件人：#{RECIPIENT_EMAIL}"
      puts "  主题：Ruby 纯文本邮件测试"
      puts "  正文：这是一封使用 Ruby 发送的纯文本邮件。"
      puts "  （注：未实际发送，仅展示示例）"
      
      # 实际发送邮件（默认注释掉，防止误发）
      # mail.deliver!
      # puts "纯文本邮件发送成功！"
      
    rescue => e
      puts "纯文本邮件示例生成失败：#{e.message}"
      puts e.backtrace
    end
  end
  
  # 发送HTML格式邮件
  # 创建并发送包含HTML内容的邮件
  #
  # 注意：默认注释掉实际发送代码，防止误发
  def send_html_email
    begin
      # HTML邮件正文
      html_content = <<-HTML
<html>
<body>
  <h1>Ruby HTML邮件测试</h1>
  <p>这是一封使用 Ruby 发送的 HTML 格式邮件。</p>
  <p>可以包含 <a href="https://www.ruby-lang.org">链接</a> 和 <strong>格式化文本</strong>。</p>
</body>
</html>
      HTML
      
      # 创建邮件
      mail = Mail.new do
        from     "#{SENDER_NAME} <#{SENDER_EMAIL}>"
        to       "#{RECIPIENT_NAME} <#{RECIPIENT_EMAIL}>"
        subject  'Ruby HTML邮件测试'
        html_part do
          content_type 'text/html; charset=UTF-8'
          body html_content
        end
      end
      
      # 显示邮件内容信息
      puts "HTML邮件内容已准备好："
      puts "  发件人：#{SENDER_EMAIL}"
      puts "  收件人：#{RECIPIENT_EMAIL}"
      puts "  主题：Ruby HTML邮件测试"
      puts "  HTML正文长度：#{html_content.length} 字符"
      puts "  （注：未实际发送，仅展示示例）"
      
      # 实际发送邮件（默认注释掉，防止误发）
      # mail.deliver!
      # puts "HTML邮件发送成功！"
      
    rescue => e
      puts "HTML邮件示例生成失败：#{e.message}"
      puts e.backtrace
    end
  end
  
  # 发送带附件的邮件
  # 创建并发送包含附件的邮件
  #
  # 注意：默认注释掉实际发送代码，防止误发
  def send_email_with_attachment
    begin
      # 附件文件路径
      attachment_file = 'hundred_chickens.rb'
      
      # 创建邮件
      mail = Mail.new do
        from     "#{SENDER_NAME} <#{SENDER_EMAIL}>"
        to       "#{RECIPIENT_NAME} <#{RECIPIENT_EMAIL}>"
        subject  'Ruby 带附件邮件测试'
        body     '这是一封带附件的邮件，附件为测试文件。'
        
        # 添加附件（如果文件存在）
        if File.exist?(attachment_file)
          add_file attachment_file
          puts "  已添加附件：#{attachment_file}"
        else
          puts "  附件文件不存在：#{attachment_file}"
        end
      end
      
      # 显示邮件内容信息
      puts "带附件的邮件内容已准备好："
      puts "  发件人：#{SENDER_EMAIL}"
      puts "  收件人：#{RECIPIENT_EMAIL}"
      puts "  主题：Ruby 带附件邮件测试"
      puts "  正文：这是一封带附件的邮件，附件为测试文件。"
      puts "  （注：未实际发送，仅展示示例）"
      
      # 实际发送邮件（默认注释掉，防止误发）
      # mail.deliver!
      # puts "带附件的邮件发送成功！"
      
    rescue => e
      puts "带附件的邮件示例生成失败：#{e.message}"
      puts e.backtrace
    end
  end
end

# 程序入口点
# 演示三种邮件发送功能
if __FILE__ == $0
  puts "Ruby 发送邮件示例"
  puts "=================="
  puts "\n注意：此示例使用占位符配置，请替换为实际配置后再发送邮件。"
  
  # 创建邮件发送器实例
  sender = EmailSender.new
  
  # 演示发送纯文本邮件
  puts "\n1. 演示发送纯文本邮件："
  sender.send_text_email
  
  # 演示发送HTML格式邮件
  puts "\n2. 演示发送HTML格式邮件："
  sender.send_html_email
  
  # 演示发送带附件的邮件
  puts "\n3. 演示发送带附件的邮件："
  sender.send_email_with_attachment
  
  puts "\n所有演示完成！"
  puts "\n实际使用时，请："
  puts "1. 安装依赖：gem install mail net-smtp"
  puts "2. 替换SMTP服务器配置（服务器地址、端口、用户名、密码）"
  puts "3. 替换发件人和收件人邮箱地址"
  puts "4. 根据需要修改邮件内容"
  puts "5. 取消相关注释以实际发送邮件"
end