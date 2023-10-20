
// ORDENA NUMÉRICAMENTE
function sortTable(n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("tablaIndexable");
    switching = true;
    // Set the sorting direction to ascending:
    dir = "asc";
    /* Make a loop that will continue until
    no switching has been done: */
    while (switching) {
        // Start by saying: no switching is done:
        switching = false;
        rows = table.rows;
        
        /* Loop through all table rows (except the
        first, which contains table headers): */
        for (i = 1; i < (rows.length - 1); i++) {
            // Start by saying there should be no switching:
            shouldSwitch = false;
            /* Get the two elements you want to compare,
            one from the current row and one from the next: */
            x = parseFloat(rows[i].getElementsByTagName("TD")[n].textContent);
            y = parseFloat(rows[i + 1].getElementsByTagName("TD")[n].textContent);
            /* Check if the two rows should switch place,
            based on the direction, asc or desc: */
            if (dir == "asc") {
                if (x > y) {
                    // If so, mark as a switch and break the loop:
                    shouldSwitch = true;
                    break;
                }
            } else if (dir == "desc") {
                if (x < y) {
                    // If so, mark as a switch and break the loop:
                    shouldSwitch = true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            /* If a switch has been marked, make the switch
            and mark that a switch has been done: */
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            // Each time a switch is done, increase this count by 1:
            switchcount++;
        } else {
            /* If no switching has been done AND the direction is "asc",
            set the direction to "desc" and run the while loop again. */
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
            }
        }
    }
}

// ORDENA ALFABÉTICAMENTE
function sortTableText(n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("tablaIndexable");
    switching = true;
    // Set the sorting direction to ascending:
    dir = "asc";
    /* Make a loop that will continue until
    no switching has been done: */
    while (switching) {
    // Start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /* Loop through all table rows (except the
    first, which contains table headers): */
    for (i = 1; i < (rows.length - 1); i++) {
        // Start by saying there should be no switching:
        shouldSwitch = false;
        /* Get the two elements you want to compare,
        one from current row and one from the next: */
        x = rows[i].getElementsByTagName("TD")[n];
        y = rows[i + 1].getElementsByTagName("TD")[n];
        /* Check if the two rows should switch place,
        based on the direction, asc or desc: */
        if (dir == "asc") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
            // If so, mark as a switch and break the loop:
            shouldSwitch = true;
            break;
        }
        } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
            // If so, mark as a switch and break the loop:
            shouldSwitch = true;
            break;
        }
        }
    }
    if (shouldSwitch) {
        /* If a switch has been marked, make the switch
        and mark that a switch has been done: */
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
        // Each time a switch is done, increase this count by 1:
        switchcount ++;
    } else {
        /* If no switching has been done AND the direction is "asc",
        set the direction to "desc" and run the while loop again. */
        if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
        }
    }
    }
}

function sortTableDate(n) {
var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
table = document.getElementById("tablaIndexable");
switching = true;
// Set the sorting direction to ascending:
dir = "asc";
/* Make a loop that will continue until
no switching has been done: */
while (switching) {
    // Start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /* Loop through all table rows (except the
    first, which contains table headers): */
    for (i = 1; i < (rows.length - 1); i++) {
    // Start by saying there should be no switching:
    shouldSwitch = false;
    /* Get the two elements you want to compare,
    one from current row and one from the next: */
    x = rows[i].getElementsByTagName("TD")[n];
    y = rows[i + 1].getElementsByTagName("TD")[n];
    /* Check if the two rows should switch place,
    based on the direction, asc or desc: */
    if (dir == "asc") {
        if (compareDates(x.textContent, y.textContent) > 0) {
        // If so, mark as a switch and break the loop:
        shouldSwitch = true;
        break;
        }
    } else if (dir == "desc") {
        if (compareDates(x.textContent, y.textContent) < 0) {
        // If so, mark as a switch and break the loop:
        shouldSwitch = true;
        break;
        }
    }
    }
    if (shouldSwitch) {
    /* If a switch has been marked, make the switch
    and mark that a switch has been done: */
    rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
    switching = true;
    // Each time a switch is done, increase this count by 1:
    switchcount++;
    } else {
    /* If no switching has been done AND the direction is "asc",
    set the direction to "desc" and run the while loop again. */
    if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
    }
    }
}
}

function compareDates(date1, date2) {
    // This function parses and compares dates in the format "14 de Julio de 2010"
    const months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];

    const dateParts1 = date1.split(" de ");
    const dateParts2 = date2.split(" de ");

    const day1 = parseInt(dateParts1[0]);
    const month1 = months.indexOf(dateParts1[1]);
    const year1 = parseInt(dateParts1[2]);

    const day2 = parseInt(dateParts2[0]);
    const month2 = months.indexOf(dateParts2[1]);
    const year2 = parseInt(dateParts2[2]);

    if (year1 < year2) {
    return -1;
    } else if (year1 > year2) {
    return 1;
    } else {
    if (month1 < month2) {
        return -1;
    } else if (month1 > month2) {
        return 1;
    } else {
        if (day1 < day2) {
        return -1;
        } else if (day1 > day2) {
        return 1;
        } else {
        return 0;
        }
    }
    }
}