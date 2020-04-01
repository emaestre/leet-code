/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = (nums, target) => {
	const hashMap = {};
	const result = [];
	let difference;

	for (let index = 0; index < nums.length; index++) {
		difference = target - nums[index];
		if (difference in hashMap) {
			result[0] = index;
			result[1] = hashMap[difference];
			return result;
		}

		hashMap[nums[index]] = index;
	}

	return result;
};
