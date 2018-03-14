<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html>
<html>
<head>
    <title>PersonaliTea</title>
    <link href="webjars/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">

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


        #header {
            height: 90px;
            font-family: Courier;
            margin-top: -20px;
            margin-left: 25px;
            margin-right: 25px;
        }


        #title {
            font-size: 45px;
            color: darkgreen;
        }

        #welcome {
            margin-left: 35px;
            color: darkgreen;

        }

        .navbar{
            margin-top: -20px;
            margin-left: 25px;
            margin-right: 25px;
        }

        body {
            background: url(https://images2.imgbox.com/b7/fb/9wluKyRB_o.jpg);
        }

    </style>
</head>
<body>
    <div class="page-header" id="header">
        <br><p id="title">PersonaliTea.com</p>
    </div>


    <nav class="navbar navbar-default">

        <a class="navbar-brand" href="#"><span class="glyphicon glyphicon-leaf" aria-hidden="true"></span></a>
        <ul class="nav navbar-nav">
            <li class="active"><a href="#">Home</a></li>
            <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false"><span class="glyphicon glyphicon-eye-open" aria-hidden="true"></span> Guardians<span class="caret"></span></a>
                <ul class="dropdown-menu">
                    <li><a href="#">ESTJ</a></li>
                    <li><a href="#">ESFJ</a></li>
                    <li><a href="#">ISTJ</a></li>
                    <li><a href="#">ISFJ</a></li>
                </ul>
            </li>
            <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false"><span class="glyphicon glyphicon-knight" aria-hidden="true"></span> Rationals<span class="caret"></span></a>
                <ul class="dropdown-menu">
                    <li><a href="#">ENTJ</a></li>
                    <li><a href="#">ENTP</a></li>
                    <li><a href="#">INTJ</a></li>
                    <li><a href="#">INTP</a></li>
                </ul>
            </li>
            <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false"><span class="glyphicon glyphicon-music" aria-hidden="true"></span> Artisans<span class="caret"></span></a>
                <ul class="dropdown-menu">
                    <li><a href="#">ESTP</a></li>
                    <li><a href="#">ESFP</a></li>
                    <li><a href="#">ISTP</a></li>
                    <li><a href="#">ISFP</a></li>
                </ul>
            </li>
            <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false"><span class="glyphicon glyphicon-globe" aria-hidden="true"></span> Idealists<span class="caret"></span></a>
                <ul class="dropdown-menu">
                    <li><a href="#">ENFJ</a></li>
                    <li><a href="#">ENFP</a></li>
                    <li><a href="#">INFJ</a></li>
                    <li><a href="#">INFP</a></li>
                </ul>
            </li>
        </ul>

        <div class="container-fluid">
            <ul class="nav navbar-nav navbar-right">
                <li><a href="/login.do">Login</a></li>
            </ul>
        </div>


    </nav>

<div class="container" id="welcome">
    <strong>Welcome, ${username}!</strong>
</div>

<footer class="footer">
    <p><strong>&copy; 2018 PersonaliTea.com</strong></p>
</footer>

<script src="webjars/jquery/1.9.1/jquery.min.js"></script>
<script src="webjars/popper.js/1.12.5/dist/popper.min.js"></script>
<script src="webjars/bootstrap/3.3.6/js/bootstrap.min.js"></script>

</body>

</html>


<%--
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <link href="webjars/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
    <title>PersonaliTea</title>
</head>
<body>
    <p>Welcome, ${username}!</p>
    <p>Personality Types</p>
    <ol>
        <c:forEach items="${personalityTypeList}" var="personalityType">
            <li>${personalityType.name} &nbsp; &nbsp; <a href="/delete-type.do?personalityType=${personalityType.name}">Delete</a></li>
        </c:forEach>
    </ol>
    <form action="/add-type.do" method="post">
        <input type="text" name="personalityType"><input type="submit" value="Add Type">
    </form>

<script src="webjars/jquery/1.9.1/jquery.min.js"></script>
<script src="webjars/bootstrap/3.3.6/js/bootstrap.min.js"></script>
</body>
</html>
--%>