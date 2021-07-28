const server_url = "../message/";
const suggestion_url = "../suggestion/";

var element = $('.floating-chat');
var myStorage = localStorage;

if (!myStorage.getItem('chatID')) {
    myStorage.setItem('chatID', createUUID());
}

setTimeout(function() {
    element.addClass('enter');
}, 1000);

element.click(openElement);


function openElement() {
    let messages = element.find('.messages');
    let textInput = element.find('.text-box');
    element.find('>i').hide();
    element.addClass('expand');
    element.find('.chat').addClass('enter');
    let strLength = textInput.val().length * 2;
    textInput.keydown(onMetaAndEnter).prop("disabled", false).focus();
    element.off('click', openElement);
    element.find('.header button').click(closeElement);
    element.find('#sendMessage').click(sendNewMessage);
    messages.scrollTop(messages.prop("scrollHeight"));
}

function closeElement() {
    element.find('.chat').removeClass('enter').hide();
    element.find('>i').show();
    element.removeClass('expand');
    element.find('.header button').off('click', closeElement);
    element.find('#sendMessage').off('click', sendNewMessage);
    element.find('.text-box').off('keydown', onMetaAndEnter).prop("disabled", true).blur();
    setTimeout(function() {
        element.find('.chat').removeClass('enter').show()
        element.click(openElement);
    }, 500);
}

function createUUID() {
    // http://www.ietf.org/rfc/rfc4122.txt
    let s = [];
    let hexDigits = "0123456789abcdef";
    for (let i = 0; i < 36; i++) {
        s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
    }
    s[14] = "4"; // bits 12-15 of the time_hi_and_version field to 0010
    s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1); // bits 6-7 of the clock_seq_hi_and_reserved to 01
    s[8] = s[13] = s[18] = s[23] = "-";

    let uuid = s.join("");
    return uuid;
}

function sendNewMessage() {
    let userInput = document.getElementById('chat_text_in');
    let newMessage = userInput.value;
    console.log(newMessage);

    if (!newMessage){
        return;
    }

    let messagesContainer = $('.messages');

    messagesContainer.append([
        '<li class="self">',
        newMessage,
        '</li>'
    ].join(''));

    // clean out old message
    send_message(newMessage);
    userInput.value = '';
    // focus on input
    userInput.focus();

    messagesContainer.finish().animate({
        scrollTop: messagesContainer.prop("scrollHeight")
    }, 250);
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function send_message(message) {
    let json_data = {
        sender: "user1",
        message: message
    }
    let chat_bubble = $('.chat-bubble');
    let text_data = JSON.stringify(json_data)
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var messagesContainer = $('.messages');
            let rasa_txt = JSON.parse(this.responseText)["text"];
            messagesContainer.append([
                '<li class="other">',
                rasa_txt,
                '</li>'
            ].join(''));
            messagesContainer.finish().animate({
                scrollTop: messagesContainer.prop("scrollHeight")
            }, 250);
        }
        else{

        }
        document.getElementById("chat_bubble").style.display = "none";
    };
    xhr.open("POST", server_url, true);
    document.getElementById("chat_bubble").style.display = "inline";
    let csrftoken = getCookie('csrftoken');
    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.send(text_data);

}

function onMetaAndEnter(event) {
    if ((event.metaKey || event.ctrlKey) && event.keyCode == 13) {
        sendNewMessage();
    }
}


function get_suggested_question(chat_text, inp, a){
    let text_data = JSON.stringify({chat_text: chat_text})
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let suggestions = JSON.parse(this.responseText)["suggestions"];
            let in_words = chat_text.toLowerCase().split(" ");
            for (i = 0; i < suggestions.length; i++) {
                let sg_words = suggestions[i].toLowerCase().split(" ");
                b = document.createElement("DIV");
                for (j = 0; j < sg_words.length; j++){
                    if (in_words.includes(sg_words[j]))
                        b.innerHTML += "<strong>" + sg_words[j] + "</strong>" + " ";
                    else
                       b.innerHTML += sg_words[j] + " ";
                }
                /*insert a input field that will hold the current array item's value:*/
                b.innerHTML += "<input type='hidden' value='" + suggestions[i] + "'>";
                b.addEventListener("click", function(e) {
                  inp.value = this.getElementsByTagName("input")[0].value;
                  sendNewMessage();

                });
                a.appendChild(b);
            }
        }
        else{

        }
        document.getElementById("chat_bubble").style.display = "none";
    };
    xhr.open("POST", suggestion_url, true);
    document.getElementById("chat_bubble").style.display = "inline";
    let csrftoken = getCookie('csrftoken');
    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.send(text_data);
    return;
}

function autocomplete() {
  let inp = document.getElementById("chat_text_in")
  let currentFocus = 0;

  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function(e) {
      let a, b, i, val = this.value;
      if (!val) return false;
      if (val.length < 5)  return false;
//      if (e.keyCode == 32 || e.keyCode == 8) return false;
      closeAllLists();
      currentFocus = -1;
      a = document.createElement("DIV");
      a.setAttribute("id", this.id + "autocomplete-list");
      a.setAttribute("class", "autocomplete-items");
      this.parentNode.appendChild(a);
      get_suggested_question(val, inp, a);
  });
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", function(e) {
      let x = document.getElementById(this.id + "autocomplete-list");
      if (x) x = x.getElementsByTagName("div");
      if (e.keyCode == 40) {
        /*arrow DOWN key is pressed*/
        currentFocus++;
        addActive(x);
      } else if (e.keyCode == 38) { //up
        /*arrow UP key is pressed*/
        currentFocus--;
        addActive(x);
      } else if (e.keyCode == 13) {
        /*ENTER key is pressed*/
        e.preventDefault();
        if (currentFocus > -1) {
          if (x) x[currentFocus].click();
        }
        closeAllLists();
        sendNewMessage();
      }
  });

  function addActive(x) {
    if (!x) return false;
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    x[currentFocus].classList.add("autocomplete-active");
  }

  function removeActive(x) {
    for (let i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }

  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    let x = document.getElementsByClassName("autocomplete-items");
    for (let i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }

  /*execute a function when someone clicks in the document:*/
  document.addEventListener("click", function (e) {
      closeAllLists(e.target);
  });
  console.log("Initiated....");
}

autocomplete();