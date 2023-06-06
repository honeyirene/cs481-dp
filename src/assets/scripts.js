if (!window.dash_clientside) {
    window.dash_clientside = {};
}
window.dash_clientside.clientside = {
    updateGraphs: function (values, ...figs) {
        const rangeMinSec = values[0];
        const currentSec = values[1];
        const rangeMaxSec = values[2];

        const rangeSize = rangeMaxSec - rangeMinSec;
        const currentX = (currentSec - rangeMinSec) / rangeSize;

        const xaxis_big_gap = {
            range: [rangeMinSec, rangeMaxSec],
            tickmode: "array",
            tickvals: [
                0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330,
                360, 390, 420, 450, 480, 510, 540, 570, 600, 630,
            ],
            ticktext: [
                "00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30",
                "04:00", "04:30", "05:00", "05:30", "06:00", "06:30", "07:00", "07:30",
                "08:00", "08:30", "09:00", "09:30", "10:00", "10:30",
            ],
        }

        const xaixs_small_gap = {
            range: [rangeMinSec, rangeMaxSec],
            tickmode: "array",
            tickvals: [0, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600,],
            ticktext: [
                "00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00",
                "08:00", "09:00", "10:00",
            ],
        }

        let newFigs = [];
        for (const fig of figs) {
            // TODO.
            const newLayout = {
                ...fig.layout,
                xaxis: rangeSize > 300 ? xaxis_big_gap : xaixs_small_gap,
                shapes: [{
                    type: "line",
                    xref: "paper",
                    yref: "paper",
                    x0: currentX,
                    x1: currentX,
                    y0: 0,
                    y1: 1,
                    line: { width: 1 },
                }],
            }

            const newFig = Object.assign({}, fig, { layout: newLayout })
            newFigs.push(newFig);
        }

        return newFigs;
    }
}
