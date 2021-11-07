function hash(input) {
    return createHash('sha256').update(input).digest('hex');
}

let password = 'hi mom';
const hash1 = hash(password);
console.log(hash1)