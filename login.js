/**
 * Created by Administrator on 2016/12/12.
 */
$(document).ready(function () {

    $("input").focus(function () {          //*************清除输入框提示
        if ($(this).val()=="请输入用户名"){
            $(this).val("");
        }
        else if ($(this).val()=="请输入密码"){
            $(this).val("").attr("type","password");
        }
    })

    $("input").blur(function () {           //*************恢复输入框提示
        if ($(this).val()=="") {
            if ($(this).index() == 0) {
                $(this).val("请输入用户名");
            }
            else {
                $(this).attr("type", "text").val("请输入密码");
            }
        }
    })

    $("button").click(function(){
    $.post("")
    })

});