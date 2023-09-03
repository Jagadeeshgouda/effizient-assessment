const steps = Array.from(document.querySelectorAll(".step"));
const nextBtn = document.querySelectorAll(".next-btn");
const prevBtn = document.querySelectorAll(".previous-btn");
const form = document.querySelector(".form");

nextBtn.forEach((button) => {
  button.addEventListener("click", () => {
    changeStep("next");
  });
});
prevBtn.forEach((button) => {
  button.addEventListener("click", () => {
    changeStep("prev");
  });
});



function changeStep(btn) {
  let index = 0;
  const active = document.querySelector(".active");
  index = steps.indexOf(active);
  steps[index].classList.remove("active");
  if (btn === "next") {
    index++;
  } else if (btn === "prev") {
    index--;
  }
  steps[index].classList.add("active");
}

var send = function() {
  Email.send({
  Host : "smtp.elasticemail.com",
  Username : "jagadeeshgoudarayangoudr1@gmail.com",
  Password : "9EF0D8EA7AF6DB1C14E6180217C1F14B2DDB",
  To : "jagadeeshgoudayr@gmail.com",
  From : "jagadeeshgoudarayangoudr1@gmail.com",
  Subject : "New Signup!!!",
  Body : "And this is the body"
}).then(
message => alert(message)
);
};
