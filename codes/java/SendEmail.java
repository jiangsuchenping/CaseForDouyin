/**
 * Java 发送邮件示例程序
 * 
 * 项目名称：CaseForDouyin
 * 模块名称：Java邮件发送示例
 * 文件功能：演示如何使用Java的JavaMail API发送邮件
 * 
 * 功能说明：
 * 1. 发送纯文本邮件
 * 2. 发送HTML格式邮件
 * 3. 发送带附件的邮件
 * 
 * 依赖要求：
 * - JavaMail API (javax.mail)
 * - Java Activation Framework (javax.activation)
 * 
 * 使用方法：
 * 1. 修改邮件服务器配置（SMTP_HOST, SMTP_PORT, USERNAME, PASSWORD）
 * 2. 修改发件人和收件人邮箱地址
 * 3. 运行程序：javac SendEmail.java && java SendEmail
 * 
 * 安全提示：
 * - 使用占位符配置，避免暴露真实密码
 * - 实际使用时请替换为自己的邮件服务器配置
 * - 建议使用应用专用密码而非主密码
 * 
 * @author 项目开发团队
 * @version 1.0.0
 * @since 2025-12-18
 */

import javax.mail.*;
import javax.mail.internet.*;
import javax.activation.*;
import java.io.File;
import java.util.Properties;

/**
 * 邮件发送器类
 * 负责管理邮件服务器配置和发送各种类型的邮件
 * 
 * 设计原则：
 * - 单一职责原则：每个方法只负责一种邮件类型的发送
 * - 开闭原则：易于扩展新的邮件类型
 * - 依赖倒置：通过接口抽象邮件发送功能
 */
public class SendEmail {
    
    /**
     * 邮件服务器配置常量
     * 使用占位符，用户需要替换为实际配置
     */
    private static final String SMTP_HOST = "smtp.example.com";     // SMTP服务器地址
    private static final String SMTP_PORT = "587";                   // SMTP服务器端口
    private static final String USERNAME = "your_email@example.com"; // 发件人邮箱
    private static final String PASSWORD = "your_password";         // 发件人密码或授权码
    
    /**
     * 邮件内容配置常量
     * 使用占位符，用户需要替换为实际信息
     */
    private static final String SENDER_EMAIL = "your_email@example.com";   // 发件人邮箱
    private static final String SENDER_NAME = "发件人名称";                   // 发件人名称
    private static final String RECIPIENT_EMAIL = "recipient@example.com";   // 收件人邮箱
    private static final String RECIPIENT_NAME = "收件人名称";                 // 收件人名称
    
    /**
     * 主方法
     * 程序入口点，演示三种邮件发送功能
     * 
     * @param args 命令行参数（未使用）
     * @throws Exception 邮件发送过程中的异常
     */
    public static void main(String[] args) throws Exception {
        System.out.println("Java 发送邮件示例");
        System.out.println("==================");
        System.out.println("\n注意：此示例使用占位符配置，请替换为实际配置后再发送邮件。");
        
        // 演示发送纯文本邮件
        System.out.println("\n1. 演示发送纯文本邮件：");
        sendTextEmail();
        
        // 演示发送HTML格式邮件
        System.out.println("\n2. 演示发送HTML格式邮件：");
        sendHtmlEmail();
        
        // 演示发送带附件的邮件
        System.out.println("\n3. 演示发送带附件的邮件：");
        sendEmailWithAttachment();
        
        System.out.println("\n所有演示完成！");
        System.out.println("\n实际使用时，请：");
        System.out.println("1. 替换SMTP服务器配置（服务器地址、端口、用户名、密码）");
        System.out.println("2. 替换发件人和收件人邮箱地址");
        System.out.println("3. 根据需要修改邮件内容");
        System.out.println("4. 取消相关注释以实际发送邮件");
    }
    
    /**
     * 获取邮件会话配置
     * 创建并配置用于发送邮件的会话对象
     * 
     * @return 配置好的邮件会话对象
     */
    private static Session getMailSession() {
        // 设置邮件服务器属性
        Properties props = new Properties();
        props.put("mail.smtp.host", SMTP_HOST);
        props.put("mail.smtp.port", SMTP_PORT);
        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.starttls.enable", "true");
        props.put("mail.smtp.connectiontimeout", "5000");
        props.put("mail.smtp.timeout", "5000");
        
        // 创建会话对象
        return Session.getInstance(props, new Authenticator() {
            @Override
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication(USERNAME, PASSWORD);
            }
        });
    }
    
    /**
     * 发送纯文本邮件
     * 创建并发送简单的纯文本邮件
     * 
     * 注意：默认注释掉实际发送代码，防止误发
     * 
     * @throws MessagingException 邮件发送异常
     */
    private static void sendTextEmail() throws MessagingException {
        try {
            // 创建邮件会话
            Session session = getMailSession();
            
            // 创建邮件消息
            Message message = new MimeMessage(session);
            message.setFrom(new InternetAddress(SENDER_EMAIL, SENDER_NAME, "UTF-8"));
            message.setRecipient(Message.RecipientType.TO, 
                               new InternetAddress(RECIPIENT_EMAIL, RECIPIENT_NAME, "UTF-8"));
            message.setSubject("Java 纯文本邮件测试", "UTF-8");
            message.setText("这是一封使用 Java 发送的纯文本邮件。", "UTF-8");
            
            // 显示邮件内容信息
            System.out.println("纯文本邮件内容已准备好：");
            System.out.println("  发件人：" + SENDER_EMAIL);
            System.out.println("  收件人：" + RECIPIENT_EMAIL);
            System.out.println("  主题：Java 纯文本邮件测试");
            System.out.println("  正文：这是一封使用 Java 发送的纯文本邮件。");
            System.out.println("  （注：未实际发送，仅展示示例）");
            
            // 实际发送邮件（默认注释掉，防止误发）
            // Transport.send(message);
            // System.out.println("纯文本邮件发送成功！");
            
        } catch (Exception e) {
            System.err.println("纯文本邮件示例生成失败：" + e.getMessage());
            e.printStackTrace();
        }
    }
    
    /**
     * 发送HTML格式邮件
     * 创建并发送包含HTML内容的邮件
     * 
     * 注意：默认注释掉实际发送代码，防止误发
     * 
     * @throws MessagingException 邮件发送异常
     */
    private static void sendHtmlEmail() throws MessagingException {
        try {
            // 创建邮件会话
            Session session = getMailSession();
            
            // 创建邮件消息
            Message message = new MimeMessage(session);
            message.setFrom(new InternetAddress(SENDER_EMAIL, SENDER_NAME, "UTF-8"));
            message.setRecipient(Message.RecipientType.TO, 
                               new InternetAddress(RECIPIENT_EMAIL, RECIPIENT_NAME, "UTF-8"));
            message.setSubject("Java HTML邮件测试", "UTF-8");
            
            // HTML邮件正文
            String htmlContent = "<html>\n" +
                               "<body>\n" +
                               "<h1>Java HTML邮件测试</h1>\n" +
                               "<p>这是一封使用 Java 发送的 HTML 格式邮件。</p>\n" +
                               "<p>可以包含 <a href=\"https://www.java.com\">链接</a> 和 <strong>格式化文本</strong>。</p>\n" +
                               "</body>\n" +
                               "</html>";
            
            message.setContent(htmlContent, "text/html; charset=UTF-8");
            
            // 显示邮件内容信息
            System.out.println("HTML邮件内容已准备好：");
            System.out.println("  发件人：" + SENDER_EMAIL);
            System.out.println("  收件人：" + RECIPIENT_EMAIL);
            System.out.println("  主题：Java HTML邮件测试");
            System.out.println("  HTML正文长度：" + htmlContent.length() + " 字符");
            System.out.println("  （注：未实际发送，仅展示示例）");
            
            // 实际发送邮件（默认注释掉，防止误发）
            // Transport.send(message);
            // System.out.println("HTML邮件发送成功！");
            
        } catch (Exception e) {
            System.err.println("HTML邮件示例生成失败：" + e.getMessage());
            e.printStackTrace();
        }
    }
    
    /**
     * 发送带附件的邮件
     * 创建并发送包含附件的邮件
     * 
     * 注意：默认注释掉实际发送代码，防止误发
     * 
     * @throws MessagingException 邮件发送异常
     */
    private static void sendEmailWithAttachment() throws MessagingException {
        try {
            // 创建邮件会话
            Session session = getMailSession();
            
            // 创建多部分邮件消息
            Message message = new MimeMessage(session);
            message.setFrom(new InternetAddress(SENDER_EMAIL, SENDER_NAME, "UTF-8"));
            message.setRecipient(Message.RecipientType.TO, 
                               new InternetAddress(RECIPIENT_EMAIL, RECIPIENT_NAME, "UTF-8"));
            message.setSubject("Java 带附件邮件测试", "UTF-8");
            
            // 创建多部分消息
            Multipart multipart = new MimeMultipart();
            
            // 添加正文
            BodyPart messageBodyPart = new MimeBodyPart();
            messageBodyPart.setText("这是一封带附件的邮件，附件为测试文件。", "UTF-8");
            multipart.addBodyPart(messageBodyPart);
            
            // 添加附件
            BodyPart attachmentBodyPart = new MimeBodyPart();
            String attachmentFile = "HundredChickens.java";
            File file = new File(attachmentFile);
            
            if (file.exists()) {
                DataSource source = new FileDataSource(file);
                attachmentBodyPart.setDataHandler(new DataHandler(source));
                attachmentBodyPart.setFileName(MimeUtility.encodeText(file.getName(), "UTF-8", null));
                multipart.addBodyPart(attachmentBodyPart);
                System.out.println("  已添加附件：" + attachmentFile);
            } else {
                System.out.println("  附件文件不存在：" + attachmentFile);
            }
            
            message.setContent(multipart);
            
            // 显示邮件内容信息
            System.out.println("带附件的邮件内容已准备好：");
            System.out.println("  发件人：" + SENDER_EMAIL);
            System.out.println("  收件人：" + RECIPIENT_EMAIL);
            System.out.println("  主题：Java 带附件邮件测试");
            System.out.println("  正文：这是一封带附件的邮件，附件为测试文件。");
            System.out.println("  （注：未实际发送，仅展示示例）");
            
            // 实际发送邮件（默认注释掉，防止误发）
            // Transport.send(message);
            // System.out.println("带附件的邮件发送成功！");
            
        } catch (Exception e) {
            System.err.println("带附件的邮件示例生成失败：" + e.getMessage());
            e.printStackTrace();
        }
    }
}