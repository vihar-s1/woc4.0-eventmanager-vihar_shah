function validateForm()
{
    if (document.forms['getEventInfo']['eventID'].value == "")
    {
        alert('Enter Event-ID !!');
        return false;
    }
    if (document.forms['getEventInfo']['eventPassword'].value == "")
    {
        alert('Enter Password !!');
        return false;
    }
}