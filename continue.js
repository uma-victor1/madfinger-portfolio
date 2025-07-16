const get_min = (string) => {
  const new_s = [string[0]];
  for (let i = 0; i < string.length; i++) {
    if (string[i] == new_s.at(-1)) {
    } else {
      new_s.push(string[i]);
    }
  }
  return string.length - new_s.length;
};

console.log(get_min("AABBAAAAAAB"));
