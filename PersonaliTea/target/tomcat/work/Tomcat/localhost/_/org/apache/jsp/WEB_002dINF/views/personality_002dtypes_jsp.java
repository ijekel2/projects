/*
 * Generated by the Jasper component of Apache Tomcat
 * Version: Apache Tomcat/7.0.47
 * Generated at: 2018-02-13 22:51:11 UTC
 * Note: The last modified time of this file was set to
 *       the last modified time of the source file after
 *       generation to assist with modification tracking.
 */
package org.apache.jsp.WEB_002dINF.views;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;

public final class personality_002dtypes_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final javax.servlet.jsp.JspFactory _jspxFactory =
          javax.servlet.jsp.JspFactory.getDefaultFactory();

  private static java.util.Map<java.lang.String,java.lang.Long> _jspx_dependants;

  private javax.el.ExpressionFactory _el_expressionfactory;
  private org.apache.tomcat.InstanceManager _jsp_instancemanager;

  public java.util.Map<java.lang.String,java.lang.Long> getDependants() {
    return _jspx_dependants;
  }

  public void _jspInit() {
    _el_expressionfactory = _jspxFactory.getJspApplicationContext(getServletConfig().getServletContext()).getExpressionFactory();
    _jsp_instancemanager = org.apache.jasper.runtime.InstanceManagerFactory.getInstanceManager(getServletConfig());
  }

  public void _jspDestroy() {
  }

  public void _jspService(final javax.servlet.http.HttpServletRequest request, final javax.servlet.http.HttpServletResponse response)
        throws java.io.IOException, javax.servlet.ServletException {

    final javax.servlet.jsp.PageContext pageContext;
    javax.servlet.http.HttpSession session = null;
    final javax.servlet.ServletContext application;
    final javax.servlet.ServletConfig config;
    javax.servlet.jsp.JspWriter out = null;
    final java.lang.Object page = this;
    javax.servlet.jsp.JspWriter _jspx_out = null;
    javax.servlet.jsp.PageContext _jspx_page_context = null;


    try {
      response.setContentType("text/html");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;

      out.write("\n");
      out.write("<!DOCTYPE html>\n");
      out.write("<html>\n");
      out.write("<head>\n");
      out.write("    <title>PersonaliTea</title>\n");
      out.write("    <link href=\"webjars/bootstrap/3.3.6/css/bootstrap.min.css\" rel=\"stylesheet\">\n");
      out.write("\n");
      out.write("    <style>\n");
      out.write("        * {\n");
      out.write("            margin: 0;\n");
      out.write("            padding: 0;\n");
      out.write("            border: 0;\n");
      out.write("            outline: 0;\n");
      out.write("            font-size: 100%;\n");
      out.write("            vertical-align: baseline;\n");
      out.write("            background: transparent;\n");
      out.write("        }\n");
      out.write("\n");
      out.write("        .footer {\n");
      out.write("            position: absolute;\n");
      out.write("            bottom: 0;\n");
      out.write("            width: 100%;\n");
      out.write("            height: 40px;\n");
      out.write("            ");
      out.write("\n");
      out.write("            text-align: center;\n");
      out.write("            margin-left: auto;\n");
      out.write("            margin-right: auto;\n");
      out.write("        }\n");
      out.write("\n");
      out.write("\n");
      out.write("        #header {\n");
      out.write("            height: 90px;\n");
      out.write("            font-family: Courier;\n");
      out.write("            margin-top: -20px;\n");
      out.write("            margin-left: 25px;\n");
      out.write("            margin-right: 25px;\n");
      out.write("        }\n");
      out.write("\n");
      out.write("\n");
      out.write("        #title {\n");
      out.write("            font-size: 45px;\n");
      out.write("            color: darkgreen;\n");
      out.write("        }\n");
      out.write("\n");
      out.write("        #welcome {\n");
      out.write("            margin-left: 35px;\n");
      out.write("            color: darkgreen;\n");
      out.write("\n");
      out.write("        }\n");
      out.write("\n");
      out.write("        .navbar{\n");
      out.write("            margin-top: -20px;\n");
      out.write("            margin-left: 25px;\n");
      out.write("            margin-right: 25px;\n");
      out.write("        }\n");
      out.write("\n");
      out.write("        body {\n");
      out.write("            background: url(https://images2.imgbox.com/b7/fb/9wluKyRB_o.jpg);\n");
      out.write("        }\n");
      out.write("\n");
      out.write("    </style>\n");
      out.write("</head>\n");
      out.write("<body>\n");
      out.write("    <div class=\"page-header\" id=\"header\">\n");
      out.write("        <br><p id=\"title\">PersonaliTea.com</p>\n");
      out.write("    </div>\n");
      out.write("\n");
      out.write("\n");
      out.write("    <nav class=\"navbar navbar-default\">\n");
      out.write("\n");
      out.write("        <a class=\"navbar-brand\" href=\"#\"><span class=\"glyphicon glyphicon-leaf\" aria-hidden=\"true\"></span></a>\n");
      out.write("        <ul class=\"nav navbar-nav\">\n");
      out.write("            <li class=\"active\"><a href=\"#\">Home</a></li>\n");
      out.write("            <li class=\"dropdown\">\n");
      out.write("                <a href=\"#\" class=\"dropdown-toggle\" data-toggle=\"dropdown\" role=\"button\" aria-haspopup=\"true\" aria-expanded=\"false\"><span class=\"glyphicon glyphicon-eye-open\" aria-hidden=\"true\"></span> Guardians<span class=\"caret\"></span></a>\n");
      out.write("                <ul class=\"dropdown-menu\">\n");
      out.write("                    <li><a href=\"#\">ESTJ</a></li>\n");
      out.write("                    <li><a href=\"#\">ESFJ</a></li>\n");
      out.write("                    <li><a href=\"#\">ISTJ</a></li>\n");
      out.write("                    <li><a href=\"#\">ISFJ</a></li>\n");
      out.write("                </ul>\n");
      out.write("            </li>\n");
      out.write("            <li class=\"dropdown\">\n");
      out.write("                <a href=\"#\" class=\"dropdown-toggle\" data-toggle=\"dropdown\" role=\"button\" aria-haspopup=\"true\" aria-expanded=\"false\"><span class=\"glyphicon glyphicon-knight\" aria-hidden=\"true\"></span> Rationals<span class=\"caret\"></span></a>\n");
      out.write("                <ul class=\"dropdown-menu\">\n");
      out.write("                    <li><a href=\"#\">ENTJ</a></li>\n");
      out.write("                    <li><a href=\"#\">ENTP</a></li>\n");
      out.write("                    <li><a href=\"#\">INTJ</a></li>\n");
      out.write("                    <li><a href=\"#\">INTP</a></li>\n");
      out.write("                </ul>\n");
      out.write("            </li>\n");
      out.write("            <li class=\"dropdown\">\n");
      out.write("                <a href=\"#\" class=\"dropdown-toggle\" data-toggle=\"dropdown\" role=\"button\" aria-haspopup=\"true\" aria-expanded=\"false\"><span class=\"glyphicon glyphicon-music\" aria-hidden=\"true\"></span> Artisans<span class=\"caret\"></span></a>\n");
      out.write("                <ul class=\"dropdown-menu\">\n");
      out.write("                    <li><a href=\"#\">ESTP</a></li>\n");
      out.write("                    <li><a href=\"#\">ESFP</a></li>\n");
      out.write("                    <li><a href=\"#\">ISTP</a></li>\n");
      out.write("                    <li><a href=\"#\">ISFP</a></li>\n");
      out.write("                </ul>\n");
      out.write("            </li>\n");
      out.write("            <li class=\"dropdown\">\n");
      out.write("                <a href=\"#\" class=\"dropdown-toggle\" data-toggle=\"dropdown\" role=\"button\" aria-haspopup=\"true\" aria-expanded=\"false\"><span class=\"glyphicon glyphicon-globe\" aria-hidden=\"true\"></span> Idealists<span class=\"caret\"></span></a>\n");
      out.write("                <ul class=\"dropdown-menu\">\n");
      out.write("                    <li><a href=\"#\">ENFJ</a></li>\n");
      out.write("                    <li><a href=\"#\">ENFP</a></li>\n");
      out.write("                    <li><a href=\"#\">INFJ</a></li>\n");
      out.write("                    <li><a href=\"#\">INFP</a></li>\n");
      out.write("                </ul>\n");
      out.write("            </li>\n");
      out.write("        </ul>\n");
      out.write("\n");
      out.write("        <div class=\"container-fluid\">\n");
      out.write("            <ul class=\"nav navbar-nav navbar-right\">\n");
      out.write("                <li><a href=\"/login.do\">Login</a></li>\n");
      out.write("            </ul>\n");
      out.write("        </div>\n");
      out.write("\n");
      out.write("\n");
      out.write("    </nav>\n");
      out.write("\n");
      out.write("<div class=\"container\" id=\"welcome\">\n");
      out.write("    <strong>Welcome, ");
      out.write((java.lang.String) org.apache.jasper.runtime.PageContextImpl.proprietaryEvaluate("${username}", java.lang.String.class, (javax.servlet.jsp.PageContext)_jspx_page_context, null, false));
      out.write("!</strong>\n");
      out.write("</div>\n");
      out.write("\n");
      out.write("<footer class=\"footer\">\n");
      out.write("    <p><strong>&copy; 2018 PersonaliTea.com</strong></p>\n");
      out.write("</footer>\n");
      out.write("\n");
      out.write("<script src=\"webjars/jquery/1.9.1/jquery.min.js\"></script>\n");
      out.write("<script src=\"webjars/popper.js/1.12.5/dist/popper.min.js\"></script>\n");
      out.write("<script src=\"webjars/bootstrap/3.3.6/js/bootstrap.min.js\"></script>\n");
      out.write("\n");
      out.write("</body>\n");
      out.write("\n");
      out.write("</html>\n");
      out.write("\n");
      out.write("\n");
    } catch (java.lang.Throwable t) {
      if (!(t instanceof javax.servlet.jsp.SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          try { out.clearBuffer(); } catch (java.io.IOException e) {}
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
