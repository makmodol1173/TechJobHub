// document.addEventListener("DOMContentLoaded", function () {
//     const form = document.querySelector("form");

//     form.addEventListener("submit", function (event) {
//         event.preventDefault();

//         const companyName = document.getElementById("company-name").value.trim();
//         const address = document.getElementById("address").value.trim();
//         const license = document.getElementById("license").value.trim();
//         const website = document.getElementById("website").value.trim();

//         if (!companyName || !address) {
//             alert("Please fill in all required fields (Company Name and Address).");
//             return;
//         }

//         if (website) {
//             const urlPattern = /^(https?:\/\/)?([\w\-]+\.)+[\w\-]+(\/[\w\-./?%&=]*)?$/;
//             if (!urlPattern.test(website)) {
//                 alert("Please enter a valid website URL.");
//                 return;
//             }
//         }

//         alert("Company details submitted successfully!");
//     });
// });
