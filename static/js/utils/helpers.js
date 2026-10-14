export function areObjectsNull({
    objects,
}) {
    let areObjectsNull = false;

    for (const object of objects) {
        const objectIsNull = object === null || object === undefined;

        if (objectIsNull) {
            return true;
        }
    }

    return areObjectsNull;
};
