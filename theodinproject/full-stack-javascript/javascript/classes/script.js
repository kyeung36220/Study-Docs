class Person {
    static species = `Homo Sapiens`

    static speciesSentence() {
        return `Humans are classified as ${this.species()}`
    }

    constructor(firstName, lastName) { //gets set up as soon as class is invoked
        this.firstName = firstName;
        this.lastName = lastName;
        this.hasJob = false;
    }

    fullName() { //don't need this and also don't need function words
        return `${this.firstName} ${this.lastName}`;
    }

    setFirstName(firstName) {
        this.firstName = firstName;
    }

    setLastName(lastName) {
        this.lastName = lastName
    }

    set setFullName(name) {
        name = name.split(" ")
        this.setFirstName(name[0])
        this.setLastName(name[1])
    }
}

class Worker extends Person {
    constructor(firstName, lastName, job) {
        super(firstName, lastName);
        this.job = job;
        this.hasJob = true;
    }

    setJob(job) {
        this.job = job
    }

    get biography() {
        const bio = `${this.fullName} is a ${this.job}.toUpperCase`
        return bio
    }
}