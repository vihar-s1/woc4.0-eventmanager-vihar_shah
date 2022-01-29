function validateForm()
{   
    if (document.forms['organizeEventForm']['event_name'].value == ""){
        alert('Enter Event Name!!');
        return false;
    }
    if (document.forms['organizeEventForm']['location'].value == ""){
        alert('Enter Event location!!');
        return false;
    }
    if (document.forms['organizeEventForm']['startDate'].value == ""){
        alert('Enter Starting Date For Event!!');
        return false;
    }
    if (document.forms['organizeEventForm']['startTime'].value == ""){
        alert('Enter Starting Time For Event!!');
        return false;
    }
    if (document.forms['organizeEventForm']['endDate'].value == ""){
        alert('Enter Terminating Date For Event!!');
        return false;
    }
    if (document.forms['organizeEventForm']['endTime'].value == ""){
        alert('Enter Terminating Time For Event!!');
        return false;
    }
    if (document.forms['organizeEventForm']['registerByDate'].value == ""){
        alert('Enter Last Date For Registration!!');
        return false;
    }
    if (document.forms['organizeEventForm']['registerByTime'].value == ""){
        alert('Enter Time for Registration Deadline!!');
        return false;
    }
    if (document.forms['organizeEventForm']['hostEmail'].value == ""){
        alert('Enter Host Email!!');
        return false;
    }
    if (document.forms['organizeEventForm']['hostPwd'].value == ""){
        alert('Enter Password!!');
        return false;
    }

    if (document.forms['organizeEventForm']['endDate'].value < document.forms['organizeEventForm']['startDate'].value)
    {
        alert('End Date-Time Must Come After Start Date-Time !!');
        return false;
    }
    
    else if (document.forms['organizeEventForm']['endDate'].value == document.forms['organizeEventForm']['startDate'].value)
    {
        if (document.forms['organizeEventForm']['endTime'].value < document.forms['organizeEventForm']['startTime'].value)
        {
            alert('End Date-Time Must Come After Start Date-Time !!');
            return false;
        }
    }

    if (document.forms['organizeEventForm']['startDate'].value < document.forms['organizeEventForm']['registerByDate'].value)
    {
        alert('Registerations Must end Before the Start of The Event!!');
        return false;
    }
    else if (document.forms['organizeEventForm']['startDate'].value == document.forms['organizeEventForm']['registerByDate'].value)
    {
        if (document.forms['organizeEventForm']['startTime'].value < document.forms['organizeEventForm']['registerByTime'].value)
        {
            alert('Registerations Must end Before the Start of The Event!!');
            return false;
        }
    }
}