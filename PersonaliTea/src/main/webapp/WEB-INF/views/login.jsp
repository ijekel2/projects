<%--
  Created by IntelliJ IDEA.
  User: nathanjekel
  Date: 1/30/18
  Time: 10:57 AM
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <link href="webjars/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
    <title>PersonaliTea</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            border: 0;
            outline: 0;
            font-size: 100%;
            vertical-align: baseline;
            background: transparent;
        }

        body {
            background: url(https://images2.imgbox.com/b7/fb/9wluKyRB_o.jpg);
        }

        #header {
            height: 90px;
            font-family: Courier;
            margin-top: -20px;
        }


        #title {
            font-size: 45px;
            margin-left: 25px;
            color: darkgreen;
        }

        .input-group {
            width: 35%;
            margin-left: 25px;
        }

        .footer {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 40px;
            <%--background-color: #c0eb80;--%>
            text-align: center;
            margin-left: auto;
            margin-right: auto;
        }

        .warning {
            margin-left: 25px;
            color: red;
        }


    </style>

</head>
<body>
<div class="page-header" id="header">
    <br><p id="title">PersonaliTea.com</p>
</div>
<form action="/login.do" method="post">
    <p class="warning"><strong>${errorMessage}</strong></p>
    <div class="input-group input-group">
        <span class="input-group-addon" id="sizing-addon1"><span class="glyphicon glyphicon-leaf" aria-hidden="true"></span></span>
        <input type="text" name="username" class="form-control" placeholder="Username" aria-describedby="sizing-addon1">
    </div>

    <div class="input-group input-group">
        <span class="input-group-addon" id="sizing-addon1"><span class="glyphicon glyphicon-leaf" aria-hidden="true"></span></span>
        <input type="password" name="password" class="form-control" placeholder="Password" aria-describedby="sizing-addon1">
        <span class="input-group-btn">
            <button class="btn btn-default" type="submit">Login</button>
        </span>
    </div>
</form>

<footer class="footer">
    <p><strong>&copy; 2018 PersonaliTea.com</strong></p>
</footer>

<script src="webjars/jquery/1.9.1/jquery.min.js"></script>
<script src="webjars/popper.js/1.12.5/dist/popper.min.js"></script>
<script src="webjars/bootstrap/3.3.6/js/bootstrap.min.js"></script>

</body>
</html>


