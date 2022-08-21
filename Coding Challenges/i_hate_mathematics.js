// ==UserScript==
// @name         I hate mathematics solver
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Reload a page to solve the task
// @author       flame
// @match        http://challenges.ringzer0team.com:10032/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=ringzer0team.com
// @grant        none
// ==/UserScript==

window.onload =(function () {
    let solveTask = () => {
        const url = "http://challenges.ringzer0team.com:10032/?r=";
        const re = /^\d+.*/gm;
        let answer, message, values, x1, x2, x3;

        message = document.getElementsByClassName("message")[0];
        message = message.innerText;
        message = message.match(re)[0];
        values = message.split(" ");
        x1 = parseInt(values[0]);
        x2 = parseInt(values[2], 16);
        x3 = parseInt(values[4], 2);

        answer = x1 + x2 - x3;
        window.location.href = `${url}${answer}`
    };

    setTimeout(solveTask, 100);
})();