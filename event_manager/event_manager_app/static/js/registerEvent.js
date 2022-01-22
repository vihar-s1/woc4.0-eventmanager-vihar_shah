
function validateForm()
{
    if (document.forms['newParticipantForm']['name'].value == ""){
        alert("Enter Your Name !!");
        return false;
    }
    if (document.forms['newParticipantForm']['contactNum'].value == ""){
        alert("Enter Contact Number !!");
        return false;
    }
    if (document.forms['newParticipantForm']['emailID'].value == ""){
        alert("Enter Your Email-ID !!");
        return false;
    }
    if (document.forms['newParticipantForm']['Event'].value == ""){
        alert("Select One Event To Participate in !!");
        return false;
    }
    if (document.forms['newParticipantForm']['RegisterType'].value == ""){
        alert("Select Registration Type!!");
        return false;
    }
    if (document.forms['newParticipantForm']['participantCount'].value == ""){
        alert("Enter Count of Participants Joining!!");
        return false;
    }
};

function showParticipantCount()
{ document.getElementById('if_Group').style.visibility = 'visible' };

function hideParticipantCount()
{ document.getElementById('if_Group').style.visibility = 'hidden' };

