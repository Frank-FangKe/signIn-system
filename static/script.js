function doValid() {
    var form = document.form;
    var isValid = true
    if(!form.number.value){
        form.number.className="warn-input"
        form.number.placeholder="请输入您的学号"
        isValid=false
    }
    if(!form.class.value){
        form.class.className="warn-input"
        form.class.placeholder="请输入您的班级"
        isValid=false
    }
    if(!form.phoneNum.value){
        form.phoneNum.className="warn-input"
        form.phoneNum.placeholder="请输入您的电话"
        isValid=false
    }
    if(!form.user.value){
        form.user.className="warn-input"
        form.user.placeholder="请输入您的名字"
        isValid=false
    }
    if (isValid){
        document.cookie = new Date();
    }
    return isValid
}

window.onload = function () {
    if(document.cookie){
        var today =new Date();
        var lastSubmited =new Date(document.cookie);
        if(today.getDate()===lastSubmited.getDate()){
            window.location='warning'
        }
    }
}