<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="static/styles.css"> 
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined"/>
    <script src="static/script.js"></script> 
</head>
<body>

<div id="navbar">
    <a href="/"><img src="static/Logo.png" width="10%" id="logo"></a> 
    <span class="material-symbols-outlined" id="menu-icon" onclick="openNav()">shopping_cart</span>
</div>

<div id="sidebar">
    <span class="material-symbols-outlined" id="sidebar-menu-icon" onclick="closeNav()">shopping_cart</span>
    <br><br><br><br>
    <a id="sideTitle">ORDER</a>
</div>

<div class="menu" id="main">
    % for group in menu:
    <div class="row">
        % for record in group:
        <div class="column" onclick="addItem('{{record[0]}}')"><h1>{{record[0]}}</h1></div>
        % end
    </div>
    % end
</div>

</body>
</html>