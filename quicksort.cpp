#include <vector>
#include<iostream>

std::vector<int> quick_sort(std::vector<int>& arr) {
    if (arr.size() < 2) {
        return arr;
    }
    int pivot = arr[0];
    std::vector<int> less{};
    std::vector<int> greater{};

    for (int i = 1; i < arr.size(); i++) {
        if (arr[i] <= pivot) {
            less.push_back(arr[i]);
        }
        else {
            greater.push_back(arr[i]);
        }
    }

    // recursion 
    std::vector<int> sorted_less = quick_sort(less);
    std::vector<int> sorted_greater = quick_sort(greater);

    // concatinate
    std::vector<int> combined_arr;
    combined_arr.reserve(sorted_less.size() + 1 + sorted_greater.size());

    combined_arr.insert(combined_arr.end(), sorted_less.begin(), sorted_less.end());
    combined_arr.push_back(pivot);
    combined_arr.insert(combined_arr.end(), sorted_greater.begin(), sorted_greater.end());
    return combined_arr;
}
int main() {
    std::vector<int> arr{ 5, 3, 7, 5, 2 };
    std::cout << "original arr: [";
    for (int i : arr) {
        std::cout << i << " ";
    }
    std::cout << "]\n";
    std::vector<int> res = quick_sort(arr);
    std::cout << "\nsorted arr: [ ";
    for (int i : res) {
        std::cout << i << (i == res[res.size() - 1] ? "]" : ", ");
    }
}