function merged_sort(arr1, arr2) {
    let i = 0, j = 0, k = 0;

    const n1 = arr1.length;
    const n2 = arr2.length;
    const arr3 = [];

    while (i < n1 && j < n2) {
        if (arr1[i] < arr2[j]) {
            arr3.push(arr1[i]);
            i++;
        } else {
            arr3.push(arr2[j]);
            j++;
        }
    
    }
    while (i < n1) {
        arr3.push(arr1[i]);
        i++;
    }

    while (j < n2) {
        arr3.push(arr2[j]);
        j++;
    }

    return arr3;
}


const ar1 = [1, 3, 5, 7];
const ar2 = [2, 4, 6, 8];
const ar3 = merged_sort(ar1, ar2);

console.log(ar3.join(" "));