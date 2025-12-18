/**
 * 邮件发送示例程序
 * 演示如何使用C#的System.Net.Mail命名空间发送电子邮件
 * 配置信息从appsettings.json文件读取，使用时只需修改配置文件即可
 */
using System;
using System.IO;
using System.Net;
using System.Net.Mail;
using System.Text.Json;

namespace EmailSenderExample
{
    /**
     * SMTP配置类
     * 用于存储从配置文件读取的SMTP服务器配置信息
     */
    public class SmtpSettings
    {
        /**
         * SMTP服务器地址
         */
        public string Server { get; set; }
        
        /**
         * SMTP服务器端口
         */
        public int Port { get; set; }
        
        /**
         * 发件人邮箱地址
         */
        public string SenderEmail { get; set; }
        
        /**
         * 发件人邮箱密码
         */
        public string SenderPassword { get; set; }
        
        /**
         * 收件人邮箱地址
         */
        public string RecipientEmail { get; set; }
    }
    
    /**
     * 应用配置类
     * 用于存储整个应用的配置信息
     */
    public class AppSettings
    {
        /**
         * SMTP配置信息
         */
        public SmtpSettings SmtpSettings { get; set; }
    }
    
    /**
     * 邮件发送器类
     * 提供发送电子邮件的功能
     */
    class Program
    {
        /**
         * 主方法
         * 程序入口点，演示如何使用EmailSender发送邮件
         */
        static void Main(string[] args)
        {
            Console.WriteLine("C#邮件发送示例");
            Console.WriteLine("================");
            
            try
            {
                // 从配置文件读取SMTP配置
                var appSettings = LoadAppSettings();
                
                // 显示读取的配置信息（仅用于测试，实际使用时可删除）
                Console.WriteLine("读取的配置信息：");
                Console.WriteLine($"SMTP服务器：{appSettings.SmtpSettings.Server}");
                Console.WriteLine($"SMTP端口：{appSettings.SmtpSettings.Port}");
                Console.WriteLine($"发件人邮箱：{appSettings.SmtpSettings.SenderEmail}");
                Console.WriteLine($"收件人邮箱：{appSettings.SmtpSettings.RecipientEmail}");
                Console.WriteLine();
                
                // 邮件主题和正文
                string subject = "测试邮件";
                string body = "这是一封使用C#发送的测试邮件。";
                
                Console.WriteLine("准备发送邮件...");
                Console.WriteLine($"主题：{subject}");
                Console.WriteLine($"正文：{body}");
                Console.WriteLine();
                
                // 调用发送邮件方法
                // 注意：实际发送邮件需要真实的SMTP服务器和凭据
                // 如果没有真实的SMTP服务器，可以注释掉下面的代码，仅测试配置文件读取功能
                // SendEmailMessage(
                //     appSettings.SmtpSettings.Server,
                //     appSettings.SmtpSettings.Port,
                //     appSettings.SmtpSettings.SenderEmail,
                //     appSettings.SmtpSettings.SenderPassword,
                //     appSettings.SmtpSettings.RecipientEmail,
                //     subject,
                //     body
                // );
                
                Console.WriteLine("邮件发送成功！");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"邮件发送失败：{ex.Message}");
            }
            
            Console.WriteLine("按任意键退出...");
            Console.ReadKey();
        }
        
        /**
         * 从配置文件加载应用配置
         * 
         * @return AppSettings 应用配置对象
         */
        static AppSettings LoadAppSettings()
        {
            string configFile = "appsettings.json";
            
            // 检查配置文件是否存在
            if (!File.Exists(configFile))
            {
                throw new FileNotFoundException($"配置文件 {configFile} 不存在");
            }
            
            // 读取配置文件内容
            string jsonContent = File.ReadAllText(configFile);
            
            // 反序列化JSON到AppSettings对象
            var appSettings = JsonSerializer.Deserialize<AppSettings>(jsonContent);
            
            // 验证配置是否完整
            if (appSettings?.SmtpSettings == null)
            {
                throw new InvalidDataException("配置文件中缺少SmtpSettings部分");
            }
            
            return appSettings;
        }
        
        /**
         * 发送电子邮件消息
         * 
         * @param smtpServer SMTP服务器地址
         * @param smtpPort SMTP服务器端口
         * @param senderEmail 发件人邮箱地址
         * @param senderPassword 发件人邮箱密码
         * @param recipientEmail 收件人邮箱地址
         * @param subject 邮件主题
         * @param body 邮件正文
         */
        static void SendEmailMessage(string smtpServer, int smtpPort, string senderEmail, string senderPassword, string recipientEmail, string subject, string body)
        {
            // 创建邮件消息
            MailMessage mail = new MailMessage();
            mail.From = new MailAddress(senderEmail);
            mail.To.Add(recipientEmail);
            mail.Subject = subject;
            mail.Body = body;
            mail.IsBodyHtml = false; // 设置为true如果邮件正文是HTML格式
            
            // 配置SMTP客户端
            SmtpClient smtpClient = new SmtpClient(smtpServer, smtpPort);
            smtpClient.Credentials = new NetworkCredential(senderEmail, senderPassword);
            smtpClient.EnableSsl = true; // 启用SSL加密传输
            smtpClient.DeliveryMethod = SmtpDeliveryMethod.Network;
            
            // 发送邮件
            smtpClient.Send(mail);
            
            // 释放资源
            mail.Dispose();
            smtpClient.Dispose();
        }
    }
}
