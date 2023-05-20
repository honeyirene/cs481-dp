import random
from component.viewGraphComponent import ViewGraphComponent
from models.graphDataModel import GraphPlotDataModel, GraphTraceDataModel


class FakeDataFactory:
    ################ generate fake data #########################
    # https://stackoverflow.com/questions/67977231/how-to-generate-random-time-series-data-with-noise-in-python-3
    def __random_timeseries(
        self,
        initial_value: float,
        volatility: float,
        count: int,
    ) -> list:
        time_series = [
            initial_value,
        ]
        for _ in range(count):
            time_series.append(
                time_series[-1] + initial_value * random.gauss(0, 1) * volatility
            )
        return time_series

    def __init__(self):
        data_x = self.__random_timeseries(0.01, 4, 600)  # 19200
        data_y = self.__random_timeseries(0.01, 4, 600)  # 19200
        data_z = self.__random_timeseries(0.01, 4, 600)  # 19200
        data_bvp = self.__random_timeseries(0.01, 4, 600)  # 38400
        data_eda = self.__random_timeseries(0.01, 4, 600)  # 2400
        data_hr_e4 = self.__random_timeseries(0.01, 4, 600)
        data_ibi = self.__random_timeseries(0.01, 4, 600)  # 38400
        data_temp = self.__random_timeseries(36.5, 0.01, 600)  # 2400
        data_brainwave_delta = self.__random_timeseries(0.01, 4, 600)  # 75000
        data_brainwave_theta = self.__random_timeseries(0.01, 4, 600)  # 75000
        data_brainwave_low_alpha = self.__random_timeseries(0.01, 4, 600)  # 75000
        data_brainwave_high_alpha = self.__random_timeseries(0.01, 4, 600)  # 75000
        data_brainwave_low_beta = self.__random_timeseries(0.01, 4, 600)  # 75000
        data_brainwave_high_beta = self.__random_timeseries(0.01, 4, 600)  # 75000
        data_brainwave_low_gamma = self.__random_timeseries(0.01, 4, 600)  # 75000
        data_brainwave_middle_gamma = self.__random_timeseries(0.01, 4, 600)  # 75000
        data_att = self.__random_timeseries(50, 0.025, 600)
        data_med = self.__random_timeseries(50, 0.025, 600)
        data_hr_ecg = self.__random_timeseries(0.01, 4, 600)
        data_audio = self.__random_timeseries(0.01, 4, 600)

        ########### create line plot with the data ##################

        traceData_acc_x = GraphTraceDataModel("x axis", data_x)
        traceData_acc_y = GraphTraceDataModel("y axis", data_y)
        traceData_acc_z = GraphTraceDataModel("z axis", data_z)
        self.plotData_acc = GraphPlotDataModel(
            "g",
            [
                traceData_acc_x,
                traceData_acc_y,
                traceData_acc_z,
            ],
        )

        traceData_bvp = GraphTraceDataModel("BVP", data_bvp)
        self.plotData_bvp = GraphPlotDataModel("PPG", [traceData_bvp])

        traceData_eda = GraphTraceDataModel("EDA", data_eda)
        self.plotData_eda = GraphPlotDataModel("uS", [traceData_eda])

        traceData_hr_e4 = GraphTraceDataModel("E4", data_hr_e4)
        traceData_hr_ecg = GraphTraceDataModel("ECG", data_hr_ecg)
        self.plotData_hr = GraphPlotDataModel(
            "Heart Rate", [traceData_hr_e4, traceData_hr_ecg]
        )

        traceData_ibi = GraphTraceDataModel("IBI", data_ibi)
        self.plotData_ibi = GraphPlotDataModel("IBI", [traceData_ibi])

        traceData_temp = GraphTraceDataModel("℃", data_temp)
        self.plotData_temp = GraphPlotDataModel("Temperature", [traceData_temp])

        traceData_bw_high_alpha = GraphTraceDataModel(
            "high-alpha", data_brainwave_high_alpha
        )
        traceData_bw_high_beta = GraphTraceDataModel(
            "high-beta", data_brainwave_high_beta
        )
        traceData_bw_middle_gamma = GraphTraceDataModel(
            "middle-gamma", data_brainwave_middle_gamma
        )
        traceData_bw_low_alpha = GraphTraceDataModel(
            "low-alpha", data_brainwave_low_alpha
        )
        traceData_bw_low_beta = GraphTraceDataModel("low-beta", data_brainwave_low_beta)
        traceData_bw_low_gamma = GraphTraceDataModel(
            "low-gamma", data_brainwave_low_gamma
        )
        traceData_bw_delta = GraphTraceDataModel("delta", data_brainwave_delta)
        traceData_bw_theta = GraphTraceDataModel("theta", data_brainwave_theta)
        self.plotData_bw = GraphPlotDataModel(
            "relative power",
            [
                traceData_bw_high_alpha,
                traceData_bw_high_beta,
                traceData_bw_middle_gamma,
                traceData_bw_low_alpha,
                traceData_bw_low_beta,
                traceData_bw_low_gamma,
                traceData_bw_delta,
                traceData_bw_theta,
            ],
        )

        traceData_att = GraphTraceDataModel("attention", data_att)
        traceData_med = GraphTraceDataModel("meditation", data_med)
        self.plotData_etc = GraphPlotDataModel(
            "attention & meditation", [traceData_att, traceData_med]
        )

        traceData_audio = GraphTraceDataModel("audio", data_audio)
        self.plotData_audio = GraphPlotDataModel("audio", [traceData_audio])


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    # view.run_server(debug=True)
    print("skip")
