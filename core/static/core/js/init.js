$(document).ready(function () {
    $('.tabs').tabs({'onShow': reload()});
});
function reload()
{
    var instance = M.Tabs.getInstance($('.tabs'));
    alert('mh');
}